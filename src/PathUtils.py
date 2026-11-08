# Copyright (C) 2018-2026 by xcentaurix
# License: GNU General Public License v3.0


import os
from Plugins.SystemPlugins.MountCockpit.MountCockpit import MountCockpit
from .Debug import logger


def getArchiveTarget(plugin, path, target_dir):
    logger.info("plugin: %s, path: %s, target_dir: %s", plugin, path, target_dir)
    src_bookmark = MountCockpit.getInstance().getBookmark(plugin, path)
    if src_bookmark is None:
        logger.error("no bookmark found for plugin '%s', path: %s", plugin, path)
        return None
    src_sub_dir = os.path.dirname(os.path.relpath(path, src_bookmark))
    dst_bookmark = MountCockpit.getInstance().getBookmark(plugin, target_dir)
    if dst_bookmark is None:
        logger.error("no bookmark found for plugin '%s', target_dir: %s", plugin, target_dir)
        return None
    target_dir = os.path.abspath(os.path.join(dst_bookmark, src_sub_dir))
    logger.debug("target_dir: %s", target_dir)
    return target_dir


def getMoveTarget(plugin, path, target_dir):
    logger.info("same bookmark - plugin: %s, path: %s, target_dir: %s", plugin, path, target_dir)
    src_bookmark = MountCockpit.getInstance().getBookmark(plugin, path)
    if src_bookmark is None:
        logger.error("no bookmark found for plugin '%s', path: %s", plugin, path)
        return None
    dst_sub_dir = os.path.relpath(target_dir, src_bookmark)
    target_dir = os.path.abspath(os.path.join(src_bookmark, dst_sub_dir))
    logger.debug("target_dir: %s", target_dir)
    return target_dir


def getMoveToTrashcanTarget(plugin, path):
    logger.info("plugin: %s, path: %s", plugin, path)
    src_bookmark = MountCockpit.getInstance().getBookmark(plugin, path)
    if src_bookmark is None:
        logger.error("no bookmark found for plugin '%s', path: %s", plugin, path)
        return None
    src_sub_dir = os.path.relpath(path, src_bookmark)
    target_dir = os.path.dirname(os.path.abspath(os.path.join(src_bookmark, ".Trash", src_sub_dir)))
    logger.debug("target_dir: %s", target_dir)
    return target_dir


def getMoveFromTrashcanTarget(path):
    """The folder a trashcan entry goes back to: <bookmark>/.Trash/<sub dir>/<name> -> <bookmark>/<sub dir>."""
    logger.info("path: %s", path)
    trashcan = "/.Trash/"
    if trashcan in path:
        bookmark, sub_path = path.split(trashcan, 1)
        target_dir = os.path.dirname(os.path.join(bookmark, sub_path))
    else:
        target_dir = os.path.dirname(path.replace("/trashcan", ""))  # trashcan of older versions
    logger.debug("target_dir: %s", target_dir)
    return target_dir
