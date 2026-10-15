# Cache Database

The reason the list opens at once is that MovieCockpit does not read your recordings when you open it. It reads a
**SQLite database** that CacheCockpit keeps up to date. This page explains what is in it and when it changes.

## Where it is

| | |
|---|---|
| File | `moviecockpit.db` |
| Folder | The *Cache directory* setting, default `/etc/enigma2` |

If the plugin cannot read the setting, it falls back to the hidden file `/etc/enigma2/.moviecockpit.db`.

Put the folder on storage that is always present and fast, with room to grow (see [Size and speed](#size-and-speed)).
The database is closed cleanly when the box shuts down.

## What is in it

Two tables:

| Table | One row per | Holds |
|---|---|---|
| `table1` | file, folder or link | type, bookmark, full path, path relative to the bookmark, folder, file name, extension, title, programme start time, recording start and stop time, length, short and extended description, service reference, size, cut list (marks and last position), sort mode, host name |
| `table2` | cover | the base name of the entry and the picture itself as a binary blob |

Both are keyed by path, so an entry exists only once. The database is a cache: everything in it can be rebuilt
from your disks. Sort modes are also written to `.sort` files and watched positions to `.cuts` files, so a rebuild
loses nothing.

### What is scanned

Directories, links, and files with one of these extensions:

| Group | Extensions |
|---|---|
| Recordings | `.ts` `.trp` |
| Blu-ray / AVCHD | `.m2ts` `.bdmv` |
| DVD images | `.ifo` `.iso` `.img` |
| Video | `.avi` `.divx` `.f4v` `.flv` `.m4v` `.mkv` `.mov` `.mp4` `.mpeg` `.mpg` `.mts` `.vob` `.wmv` `.asf` `.stream` `.webm` |

## When it is filled and changed

| Event | What happens |
|---|---|
| **First start**, no database yet | Once the mounts are known, every mounted bookmark is scanned, one file at a time, so the box stays responsive |
| **A recording starts** | The new file is added (after a short wait for it to appear), the real recording start time is written to the `.xmeta` file, and a cover download is requested |
| **A recording ends** | The stop time is written, the entry is refreshed, and the recording is moved into its series folder if one matches |
| **Playback ends** | The new watched position is stored and the folder entry is refreshed |
| **File operations** | Entries are updated as the move / copy / delete jobs finish |
| **You press Reload cache** | All mounted bookmarks are cleared from the cache and scanned again (cached entries of unmounted bookmarks stay) |
| **Cover or TMDB change** | The affected entry is reloaded |

There is no background watcher. If you copy a file into a bookmark with another tool (FTP, Samba from a PC), it
does not show up until you press **Reload cache**.

## Reloading the cache

Use **Reload cache** (red, level 3, or the function menu) after you:

- added, removed or renamed files outside MovieCockpit,
- restored the box or the database from a backup,
- moved the *Cache directory*,
- see wrong data that a [Recording Info](Troubleshooting.md#a-time-or-length-is-wrong) check traces back to a stale cache entry.

A progress screen shows the scan. Browsing is possible during the scan but the list is incomplete until it ends.

To start completely fresh, stop Enigma2, delete `moviecockpit.db`, and start again. The first-start scan then runs
again. Your recordings and cover files are not affected.

## Size and speed

A row is small. The covers dominate the size. On a test box with 121 recordings, 8 folders and 83 covers the database is
24 MB, and the covers account for nearly all of it (about 290 KB each). Plan on roughly 0.3 MB per recording that has a
cover. Opening the list never touches the disks, which is the point: a sleeping hard disk is not spun up just to
browse.
