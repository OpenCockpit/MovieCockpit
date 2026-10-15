# Architecture

For developers. The user-facing behaviour is in the other pages; this one explains how the pieces fit together.

## The family

```
 PVR key / plugin menu
        |
  MovieCockpit (MVC)  ---- UI: list screen, menus, player, setup
        |
        +--> CacheCockpit (CAC) ---- FileManager: SQL cache, file operations
        |         |                  Recording: reacts to timers, covers, series folders
        |         +--> JobCockpit (JOC) ---- runs file operations as background jobs
        |
        +--> MountCockpit (MNC) ---- bookmarks, mount points, share availability, free space
        |
        +--> ComponentsCockpit (COC) ---- skin sources, converters, renderers
        |
        +--> CoverCockpit (COV)  [optional]  ---- cover download, via a plugin hook
             TMDBCockpit, MediathekCockpit [optional] ---- movie info, Mediathek, via plugin hooks
             PowerCockpit (POC) [optional] ---- shutdown tasks: trashcan purge, archive
```

The plugin identifies itself to the others with the id **`MVC`** (`Version.ID`). `FileManager.getInstance("MVC")`
returns the cache for it, `MountCockpit.getInstance().getMountedBookmarks("MVC")` the bookmarks. The same
infrastructure serves MediaCockpit with the id `MDC`.

## Source files of MovieCockpit

| File | Role |
|---|---|
| `plugin.py` | Plugin descriptors. At session start it replaces `InfoBar.showMovies` with the function that opens the list (weight 1, so it runs after other movie list plugins), sets the EPG language and registers the bookmarks with MountCockpit |
| `MovieCockpit.py` | The list screen: loading, navigation, selection, delete / move / copy / archive, trashcan, series folders, player start |
| `MovieCockpitActions.py` | Key actions and the four-level colour-button matrix |
| `CockpitContextMenu.py` | The function menu and the plugins menu |
| `MovieList.py` | The list source: builds the rows (`buildRow`), sorting, list modes, selection |
| `Sorting.py` | Per-folder sort mode: read, write (cache and `.sort` file), toggle |
| `ServiceCenter.py` | A stand-in for `eServiceCenter` that answers service-info requests from the cache (title, times, description, size, cover) |
| `CutList.py` | Reading and writing the cut list (`.cuts` and the cache) |
| `RecordingInfo.py` | The technical info screen |
| `MovieInfoEPG.py` | The EPG info screen with the TMDB and Mediathek buttons |
| `SetupScreen.py`, `setup.xml`, `ConfigInit.py` | Settings |
| `keymap.xml` | Maps remote keys to the action names in the `CockpitActions` context |
| `skin/default/*.ymlinc`, `skin/default/skin.xml` | The skin (see [Skinning](Skinning.md)) |

The player and many helpers are **shared sources** (`CockpitPlayer`, `CockpitSeek`, `CockpitSmartSeek`,
`CockpitCueSheet`, `CutListUtils`, `FileUtils`, `FileManagerUtils`, `ServiceUtils`, `SkinUtils`, ...). They live in the
`Common` repository and are copied into every Cockpit plugin when it is built, which is why they appear in the
plugin's folder on the box.

## Data flow of the list

```
MovieCockpit.onDialogShow
   FileManager.onDatabaseLoaded(loadList)       -> called when the scan is finished
   FileManager.onDatabaseChanged(loadList)      -> called after every cache change
   Loading spinner
loadList
   MovieList.loadList(return_dir, return_path)
      FileManager.getDirList / getFileList      (SQL, no disk access)
      sortList                                   (per folder: date or alpha, up or down)
      buildRow                                   (date text, icon, progress, picon, colours)
   Service source <- ServiceCenter               (details pane, cover, front panel)
```

The list **never** reads the disks. The only disk access in the browsing path is the existence check when you press
**OK**. Everything else is the SQL cache or the files that file jobs touch.

### Row building

`MovieList.buildRow` appends nine display values to the 20 database columns (`ROW_IDX_*` in `MovieList.py`). The
category priority for colour and progress bar is: marked or locked, then running recording, then normal. Progress is
computed from the cut list's *last* position, or from `now - event start` for a running recording, or from the
job's progress for a download.

### Selection and cursor

`getSelectionList` returns the marked entries, or the entry under the cursor. When exactly one entry is selected the
cursor is moved to the next one, so repeated use works through the list. `return_dir` and `return_path` are class
attributes on the screen, so they survive closing and reopening the plugin within one session.

## File operations

`MovieCockpit` collects `(op, path, target)` tuples and calls `FileManager.execFileOp`. For each, CacheCockpit

1. looks up the entry (and, for delete and same-disk move, every entry with the same relative path on other bookmarks),
2. checks free space for copies and cross-disk moves (free space x 0.8 must cover the size),
3. adds a job to JobCockpit; the job runs shell commands (`mv`, `cp`, `rm`, `mkdir`, helper scripts for folders) on
   all files that share the base name,
4. calls back; MovieCockpit reloads the list after a 500 ms quiet period.

Entries with a running job are in `FileManager.getLockList()`; the list shows the operation and the selection colour.

Deleting moves to `<bookmark>/.Trash/<relative folder>`; `.Trash` is excluded from the normal queries and from
archiving. `FileManager.purgeTrashcan(retention)` deletes entries older than the retention; `archive()` queues moves
from the archive source to the target bookmark. Both finish with a trim job.

## Recording hook

CacheCockpit's `Recording` class listens to `RecordTimer.on_state_change`. On a timer start it writes the
`.xmeta` file, adds the file to the cache and, if `cover_auto_download` is on, requests a cover through the
`WHERE_COVER_DOWNLOAD` plugin hook; on timer end it records the stop time, refreshes the entry and applies the
series-folder rule. If `timer_autoclean` is on, `RecordTimer.cleanup()` runs at start-up and two seconds after each
timer end (the timer only joins the processed list after the state callback has returned).

## Extension hooks

| Hook (`PluginDescriptor.where`) | Value | Used for |
|---|---|---|
| `WHERE_MOVIELIST` | standard | The long-**MENU** plugins menu |
| `WHERE_TMDB_MOVIELIST` | -97 | TMDB info (`PluginUtils.WHERE_TMDB_MOVIELIST`) |
| `WHERE_MEDIATHEK_SEARCH` | -96 | Mediathek search |
| `WHERE_COVER_DOWNLOAD` | -94 | Cover download |

`getPlugin(where)` returns the first plugin registered for a hook, or `None`; the buttons depend on the answer.

## Build, packaging, translations

- Autotools project (`Makefile.am` files); installed under `.../Plugins/Extensions/MovieCockpit`.
- `CONTROL/control` defines the package and its dependencies; `postrm` removes the plugin directory.
- Translations: `po/MovieCockpit.pot` is the template, `po/de.po` the German translation. Strings are wrapped in
  `_()` from the plugin's `__init__`; setup texts are in `setup.xml`.
- Logging: `Debug.py` sets up a logger with the prefix `MVC:` writing to stdout, so it ends up in the Enigma2
  debug log. The level is the *Log level* setting.
- Releases are listed in `.releases`; the current one is 0.19.1.

## Conventions

- Every file starts with the licence header (GPLv3), and uses `logger.info("...")` / `logger.debug(...)` at function entry.
- Row field and database column indices are named constants (`FILE_IDX_*` in `FileManagerUtils.py`); the skin uses
  the numbers, so keep both in sync.
- Anything that can block (network shares, disk operations) runs in a thread or a job; the list code only talks to SQL.
