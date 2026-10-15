# User Guide

## Opening MovieCockpit

- Press **PVR** or **VIDEO** in TV mode (this replaces the standard movie list), or
- start **MovieCockpit** ("Manage recordings") from the plugin menu.

Leave with **EXIT** (or **POWER**, **HOME**, **TV**).

Where the list opens depends on *Show bookmark content on start*. On (the default) it always opens the home
directory. Off, it opens the directory and entry you were on when you left it.

## The screen

```
+--------------------------------------------------------------+
| MovieCockpit - Videos - <folder>                             |  title bar
| [sort] Date sort down          [disk] hdd: 42.5%, usb: 18.0% |  sort mode, disk usage
|                                                              |
|  list of recordings               |  cover                   |
|  icon  title        date          |  title                   |
|        (progress bar, picon)      |  length, description,    |
|                                   |  extended description    |
|                                                              |
| <1>  Delete  | Sort mode | Move | Trashcan      Menu  Info   |  colour buttons, level
+--------------------------------------------------------------+
```

- **Title bar** shows the plugin, *Videos* (or *.Trash* inside the trashcan) and the folder relative to its bookmark.
- **Sort mode** shows how the current folder is sorted (see below).
- **Disk usage** lists the used percentage of every mounted bookmark disk.
- **Details** on the right update shortly after you stop moving the cursor (200 ms by default), so scrolling
  through a long list stays fast.
- **Colour buttons** at the bottom change meaning with the **level** shown as `<1>` ... `<4>`.
  See [Keys and Buttons](Keys-and-Buttons.md).

## What a row shows

| Part | Meaning |
|---|---|
| Icon | Folder, back arrow (`..`), link, trashcan, or a movie in one of four states (below) |
| Title | The programme title (from the EIT file, falling back to the meta file or the file name) |
| Date column | Programme start, formatted per the *date format* setting. For folders: the folder information. While a file operation runs on the entry: *Deleting*, *Moving*, *Copying* or *Loading* |
| Progress bar | How far you have watched, or how far a running recording has progressed |
| Picon | The channel logo of the recording |

### Movie icons

| State | When |
|---|---|
| Default | Not started, or less than *Watching in progress percent* watched (default 10 %) |
| Watching | At least *Watching in progress percent* watched (default 10 %) |
| Finished | At least *Finished watching percent* watched (default 90 %) |
| Recording | The recording is running right now |

### Colours

Normal entries are grey, a running recording is red, and entries that you have marked (or that a file
operation currently holds) are yellow. The highlighted row uses the matching "highlighted" colour. All six
colours can be changed in [Settings](Settings.md).

### Folder information

For folders the date column can show nothing, the word *directory*, the number of recordings in it `(12)`,
the number and total size `(12/84 GB)`, or just the size `(84 GB)`. Choose it with *Show directories information*.
The trashcan has its own setting, *Show trashcan information*. The `..` row shows *up*.

## List contents (what the list contains)

**FAST FORWARD** and **REWIND** cycle through four ways of filling the list. There is no on-screen label;
the list simply changes. The choice is remembered.

| Mode | The list shows |
|---|---|
| 0 | Recordings of the current folder only. No folders |
| 1 | Folders first, then the recordings of the current folder (default) |
| 2 | **All recordings from all folders** below the home directory, as one flat list |
| 3 | The recordings of the current folder with its sub-folders mixed in. Empty sub-folders are hidden, and a sub-folder containing exactly one recording shows that recording instead of the folder |

Mode 2 is useful to find a recording when you do not remember the folder. Mode 3 gives a compact view of series
folders.

## Sorting

Each folder remembers its own sort mode. **Green** at level 1 changes the sort mode (date or alphabetical),
and **green** at level 2 flips the order.

| Mode | Order |
|---|---|
| Date sort down | Newest first (default) |
| Date sort up | Oldest first |
| Alpha sort up | A to Z |
| Alpha sort down | Z to A |

Entries that compare equal are ordered by the other criterion (title for date sort, date for alphabetical sort).
The mode is saved in the cache and in a small `.sort` file inside the folder, so it survives a cache reload. A series folder you create yourself starts as *Date sort up*, so the episodes are in
order.

## Selecting entries

Most functions work on the **marked** entries. If nothing is marked they work on the entry under the cursor.

- **VIDEO / PVR** (short press) marks or unmarks the entry under the cursor and moves down.
- **VIDEO / PVR** (long press) unmarks everything.
- The `..` row cannot be marked.
- Marked entries are shown in the selection colour (yellow by default).

After a function runs on the entry under the cursor, the cursor moves on to the next entry, so you can
work through a list by repeating the same key.

## Playing

Press **OK** on a recording. A folder opens instead. Details are in [Playback](Playback.md). If the file does not
exist any more, a message tells you which one.

## Information screens

- **INFO** (short press) opens the **EPG info** of the programme: title, times, description, extended
  description. From there **yellow** opens the TMDB info (if TMDBCockpit is installed) and **blue** starts a
  Mediathek search/download (if MediathekCockpit is installed).
- **INFO** (long press) goes straight to the TMDB info.
- Key **5** opens **Recording Info**, a technical page listing path, file name, the times stored in the cache,
  and what the `.eit`, `.meta` and `.xmeta` files contain. It is the first place to look when a time or
  length looks wrong. See [Troubleshooting](Troubleshooting.md).

## The menus

- **MENU** (short press) opens the **function menu**: Home, Directory up, Delete, Move, Copy, Create series
  directory, Move to series directory, Empty trashcan, Delete cover, Bookmarks, Archive (if enabled), Reload
  cache, Remove all marks, Setup, About.
- **MENU** (long press) opens the **plugins menu** with every plugin that registers itself for the movie list
  (for example subtitle or convert tools). It acts on the entry under the cursor.
