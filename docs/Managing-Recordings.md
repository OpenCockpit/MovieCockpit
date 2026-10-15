# Managing Recordings

Everything on this page works on the **marked** entries, or on the entry under the cursor when nothing is marked
(see [Selecting entries](User-Guide.md#selecting-entries)).

A recording is more than one file: next to `Title.ts` there are `.eit`, `.meta`, `.xmeta`, `.cuts`, a cover
`.jpg` and so on. MovieCockpit treats all files that share the recording's base name as one unit, so delete, move
and copy always take them together.

## Deleting and the trashcan

**Delete** (red, level 1) does not remove anything at once. It **moves** the recording into the trashcan of the
disk it is on:

```
/media/hdd/movie/Series/Episode.ts
        becomes
/media/hdd/movie/.Trash/Series/Episode.ts
```

The sub-folder is kept, so the recording can go back where it came from.

- The trashcan shows as the first row of the home directory (if *Show trashcan directory* is on). Open it
  with **Trashcan** (blue, level 1).
- Inside the trashcan, **Delete** removes the entries for good, after a confirmation that lists the names.
- **Restore** (yellow, level 1, inside the trashcan) moves entries back into the folder they were deleted from.
- **Empty trashcan** (red, level 2) deletes everything in the trashcan, after a confirmation.
- Moving a recording to the trashcan updates the modification time of its files, so the retention period counts
  from the day you deleted it, not from the day it was recorded.

### Automatic clean-up

MovieCockpit itself only empties the trashcan when you ask it to. If **PowerCockpit** is installed and *Enable auto
trashcan cleanup* is on (default), it purges the trashcan whenever the box is switched off (shutdown / deep
standby). Entries older than the *File retention period in trashcan* (default 3 days, 0 to 30) are removed. With a
retention of 0, everything goes.
See [Settings](Settings.md#trashcan).

### A running recording

If a selected recording is still being recorded, **Delete** first asks *"Stop recording(s)?"*. After you answer
yes, the recording is stopped and then deleted as above. The **STOP** key on its own stops the running recordings
among the selection and does not delete them.

### One entry, several disks

Because all bookmarks are merged into one library (see [Storage and Network](Storage-and-Network.md)), a folder
that exists on more than one disk appears once in the list. **Delete**, and **Move** within one disk, apply to the entry
on every disk that has the same relative path. Remember this before deleting a "Series" folder that you
have spread over a hard disk and a NAS.

## Move and copy

**Move** (yellow, level 1) and **Copy** (yellow, level 2) open a folder chooser. It lists your bookmarks and lets
you open or create folders. System directories such as `/bin`, `/etc`, `/usr` and `/var` cannot be chosen.

- The target disk must be mounted, otherwise you get *"... is not mounted"*.
- Copying, and moving **across disks**, first check the free space. The target needs at least 1.25 times the size of
  the entries free; otherwise you get *"Not enough space in target directory for video file"* and nothing is done
  for that entry.
- **Running recordings are skipped** with a message (*Can't move recordings* / *Can't copy recordings*).
- The work runs as **background jobs** (JobCockpit). You can keep browsing. Entries that are being processed show
  *Moving*, *Copying* or *Deleting* in the date column, are shown in the selection colour, and cannot be opened.
  Pressing **OK** on one opens the progress screen. Key **8** opens it too.
- When several entries are processed, the list is refreshed once when the work calms down, not after each file.

## Series folders

MovieCockpit can keep a series together in one folder.

**Automatically.** When a recording ends, MovieCockpit looks in the folder where it was saved for a sub-folder whose
name is the **beginning of the recording's title**. If it finds one, the recording is moved into it.

Example: with a folder `Tatort`, a new recording `Tatort: Der Pott` is filed into `Tatort`. Use reasonably specific
folder names, because a folder `A` would catch every title that starts with an A.

A recording you are currently playing is not moved.

**Manually.**

- **Create series directory** (function menu) suggests a folder name taken from the title of the entry under the
  cursor: the part before the first `: ` (or, if the title has none, before ` - ` or ` (`). Edit the name on the on-screen keyboard and confirm. The
  new folder starts with *Date sort up*, so episodes are listed in order.
- **Move to series directory** (function menu) moves the marked entries into the folder that matches them by
  the rule above.

A series folder can have a cover too (see [Covers and Metadata](Covers-and-Metadata.md)).

## Archive

The archive moves finished recordings from one disk to another, for example from the internal hard disk to a
USB or NAS disk, keeping the folder structure. Typical use: record to a fast internal disk, archive to a large
one.

Set it up in [Settings](Settings.md#archive): turn on *Enable archive*, choose the **source** and the
**target** bookmark. They must both exist and must be different.

It moves every recording below the source directory to the same relative place under the target. It
skips:

- recordings that are still running,
- everything in the trashcan,
- symbolic links.

Afterwards a *trim* job runs so that flash media (SSD, SD card) are told which blocks are free.

With *Enable archive* on, start it with **Archive** (yellow, level 3, or the function menu entry), or let PowerCockpit
run it when the box is shut down. With *Enable archive* off the button and the menu entry are not shown and nothing
is archived. If a source or target directory is missing, a message tells you to fix the setup.

## Other functions

| Function | What it does |
|---|---|
| **Reset progress** (red, level 4) | Forgets the watched position of the marked entries |
| **Remove all marks** (menu) | Deletes cut-list marks of the marked entries |
| **Delete cover** (menu) | Deletes the cover image file and the cached cover |
| **Reload cache** (red, level 3) | Rescans all mounted bookmarks, see [Cache Database](Cache-Database.md) |
| **Timer list** (yellow, level 4) | Opens the Enigma2 timer list |
