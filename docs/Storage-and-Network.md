# Storage and Network

## Bookmarks

MovieCockpit does not scan the whole box. It scans the **bookmarks**: the movie directories you list. Typical
bookmarks are `/media/hdd/movie`, `/media/usb/movie`, or a directory on a NAS share such as
`/media/nas/movie`.

The first time the plugin runs, the bookmarks are copied from Enigma2's own movie directories. Change them later
with **Bookmarks** (blue, level 3, or the function menu). The chooser lets you add, remove and create directories.
When you leave it, the list is saved, the scan list is updated, and, if the directory you were in is no longer under a
bookmark, you are taken to the home directory.

System directories (`/bin`, `/boot`, `/dev`, `/etc`, `/home`, `/lib`, `/proc`, `/run`, `/sbin`, `/sys`, `/usr`,
`/var`) are refused as targets.

## One library from several disks

All bookmarks form a **virtual file system**. A folder or recording is identified by its path *relative to its
bookmark*. If `/media/hdd/movie/Series` and `/media/nas/movie/Series` both exist, the list shows **one** folder
`Series` whose content is the union of both. A recording is listed with its real location, and the **Date / Mount**
button (level 4) switches the date column to the disk name, so you can see which disk a recording is on.

Two things follow from this:

- Moving a recording inside one disk keeps it on that disk. Moving it to a folder on another bookmark copies it
  there and removes the original.
- Delete and same-disk move apply to the entry on **every** disk that has the same relative path. See
  [Managing Recordings](Managing-Recordings.md#one-entry-several-disks).

## The home directory

The **home directory** is the first bookmark that is currently available. **Home** (blue, level 2, or **0** long)
goes there. The trashcan lives in `.Trash` directly below it.

## Disks that are not there

Only **mounted and reachable** bookmarks are shown. If a USB disk is unplugged or a NAS is switched off, its
entries disappear from the list but are **not** removed from the cache. When the disk is back, its entries are
back, and no rescan is needed. A rescan (**Reload cache**) only refreshes bookmarks that are mounted at that
moment and leaves the cached entries of the others alone.

A network share that does not answer is detected after a few seconds (the free space of each bookmark is checked
every 5 seconds and given three checks to answer), so a sleeping NAS cannot freeze the list.

## Free space

The header of the list shows how full each disk is, as in `hdd: 42.5%, nas: 61.0%`. A disk that does not
answer is left out.

## Network shares that come and go (MountCockpit)

MountCockpit manages the network shares of the box (NFS and CIFS) in `/etc/enigma2/automounts.xml` and
`/etc/fstab`. Its **enabled** switch (`config.plugins.mountcockpit.enabled`, off by default) makes it ping the
hosts of your shares every 5 seconds. A share is mounted when its host answers and unmounted when it stops
answering. This is what lets a NAS that sleeps most of the day appear in MovieCockpit as soon as it wakes up, and
vanish when it is switched off, without a stuck mount. Leave it off if your shares are always available.

Shares that are mounted by other means work as well. MovieCockpit only needs the bookmark to lie on a mounted file
system of its own.

> **Note:** a bookmark on the **root file system** (the internal flash, for example `/home/root/movie`) is ignored,
> as are the pseudo file systems `/tmp`, `/dev` and so on. Use a mounted disk, USB stick, SD card or share.
