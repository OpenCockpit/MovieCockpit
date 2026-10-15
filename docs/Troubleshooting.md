# Troubleshooting

## The list is empty

- **First start?** The cache is still being built. Wait for the scan to finish. Key **8** opens the progress screen.
- **No bookmark is mounted.** The list only shows mounted bookmarks (see [Storage and Network](Storage-and-Network.md)).
  Check that the disk or share is mounted and that the bookmark is listed under **Bookmarks**.
- **The bookmark is on the internal flash** (the root file system). Such directories are ignored. Use a mounted disk.
- **You added files outside MovieCockpit.** Press **Reload cache** (red, level 3). There is no file watcher.
- **List content mode 3 or 0** is active and the folder you are in has no recordings of its own. Press
  **FAST FORWARD** / **REWIND** to change the mode.

## A recording is missing after I copied it in

MovieCockpit only learns about files it moved or recorded itself. Press **Reload cache**.

## A time or length is wrong

Select the entry and press **5** (*Recording Info*). The page lists the values side by side:

| Lines | Source |
|---|---|
| `SQL:` | What the cache holds and the list shows |
| `EIT:` | The programme as stored in the `.eit` file |
| `META:` | Enigma2's `.meta` file (record time) |
| `XMETA:` | MovieCockpit's own start and stop of the recording |

Typical findings:

- `EIT: File exists = False`. There is no programme data, so the length is unknown or comes from the meta file.
- `XMETA` is missing, or its start time equals its stop time. MovieCockpit did not see the recording start, so it
  cannot trim the margins; the programme start and length are taken straight from the EIT.
- The `SQL:` values differ from `EIT:` and `META:`. The cache entry is stale. Press **Reload cache**.

## Playback starts at the wrong place

*Video start at* chooses it (see [Playback](Playback.md)). *Event start* needs the EIT and xmeta data (see above). With *first mark*,
a recording without marks starts at the beginning.

## The resume question does not appear

- *Resume video at last position* is off.
- The recording has no saved position (never played, or **Reset progress** was used).

## Everything about a disk is greyed out or gone

The bookmark is not reachable. Check the mount. A NAS that is asleep is hidden until it answers; see
*MountCockpit* in [Storage and Network](Storage-and-Network.md#network-shares-that-come-and-go-mountcockpit).

## Covers

- **No cover is downloaded.** Install **CoverCockpit**; MovieCockpit does not download covers by itself. The
  channel must be in CoverCockpit's channel table, and the programme must exist at the chosen source.
- **A wrong cover is shown.** Select the entry, choose **Delete cover** from the function menu.
- **A folder shows no cover.** Place `FolderName.jpg` next to the folder, or `FolderName/FolderName.jpg` inside it,
  and press **Reload cache**.

## Moving or copying fails

- *"... is not mounted"*: the target disk is not mounted.
- *"Not enough space in target directory"*: the target needs at least 1.25 times the size of what you move.
- *"Can't move recordings"*: a selected recording is still running. Stop it first.

## Reporting a problem

MovieCockpit writes to the Enigma2 debug log. Lines from this plugin start with `MVC:`; the helper plugins use
`CAC:` (CacheCockpit), `MNC:` (MountCockpit), `JOC:` (JobCockpit) and `COV:` (CoverCockpit).

1. Open **Setup** and set **Log level** to `DEBUG` (expert mode). The log level is applied when you save.
2. Reproduce the problem.
3. Collect the Enigma2 debug log, usually in `/home/root/logs/`, together with the output of **Recording
   Info** for the affected entry.
4. Set the log level back to `INFO`. `DEBUG` is very verbose.

Include the plugin version (**About** in the function menu; this wiki describes 0.19.1) and the image you use.
