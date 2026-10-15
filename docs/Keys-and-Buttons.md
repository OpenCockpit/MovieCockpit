# Keys and Buttons

The list screen is fully described by the help screen of Enigma2: press **HELP** inside MovieCockpit to see
the current keys. This page is the same information in one place.

## In the list

### Navigation

| Key | Action |
|---|---|
| **UP** / **DOWN** | Cursor up / down |
| **LEFT** / **RIGHT** | Cursor one page up / down |
| **CHANNEL+** / **CHANNEL-** (bouquet) | Jump to the top / to the bottom of the list |
| **OK** | Play the recording, or open the folder |
| **0** | Directory up. In the top directory of a bookmark: go to the home directory |
| **0** (long) | Go to the home directory |
| **FAST FORWARD** | Next list content (see [User Guide](User-Guide.md#list-contents-what-the-list-contains)) |
| **REWIND** | Previous list content |
| **EXIT**, **POWER**, **HOME**, **TV** | Leave MovieCockpit |

### Selecting

| Key | Action |
|---|---|
| **VIDEO / PVR** | Mark or unmark the entry, then move down |
| **VIDEO / PVR** (long) | Unmark everything |

### Information and menus

| Key | Action |
|---|---|
| **INFO** | EPG info of the entry |
| **INFO** (long) | TMDB info (needs TMDBCockpit) |
| **MENU** | Function menu |
| **MENU** (long) | Plugins menu (plugins registered for the movie list) |
| **5** | Recording info (technical details) |
| **8** | File operations progress |
| **STOP** | Stop the selected running recording(s). Asks first |

### Colour buttons

Four colour buttons, four **levels**. The current level is shown bottom left as `<1>` to `<4>`, and the
button labels at the bottom always show what the buttons do at that level.

| Key | Action |
|---|---|
| **NEXT** | Next level (wraps from 4 to 1) |
| **PREVIOUS** | Previous level |

Pressing any colour button runs its function and then **returns to level 1**.

| Level | Red | Green | Yellow | Blue |
|---|---|---|---|---|
| **1** | Delete | Sort mode | Move (*Restore* inside the trashcan) | Trashcan (*Home* inside the trashcan) |
| **2** | Empty trashcan | Sort order | Copy | Home |
| **3** | Reload cache | - | Archive (only with *Enable archive* on) | Bookmarks |
| **4** | Reset progress | Date / Mount | Timer list | Open setup |

What the buttons do:

- **Delete** moves the entries to the trashcan. Inside the trashcan it deletes them for good, after asking.
- **Sort mode** switches between date and alphabetical sorting for the current folder. **Sort order** reverses it.
- **Move**, **Copy** ask for a target folder. **Restore** moves entries out of the trashcan.
- **Trashcan** opens the trashcan of the home bookmark. **Empty trashcan** deletes everything in it, after asking.
- **Home** goes to the home directory.
- **Reload cache** rescans all mounted bookmarks (after a confirmation).
- **Archive** moves finished recordings to the archive disk (see [Managing Recordings](Managing-Recordings.md#archive)).
- **Bookmarks** edits the list of directories MovieCockpit scans.
- **Reset progress** sets the watched position of the marked entries back to the start.
- **Date / Mount** switches the date column between the programme date and the name of the disk the file is on.
- **Timer list** opens the Enigma2 timer list.
- **Open setup** opens the [settings](Settings.md).

## In the function menu

**MENU** opens a choice list. Number keys are not used there; select with the cursor and **OK**.

| Entry | Does |
|---|---|
| Home, Directory up | Change directory (only shown when you are not in a bookmark root) |
| Delete, Move, Copy | As the colour buttons |
| Create series directory | Creates a folder named after the entry (see [Managing Recordings](Managing-Recordings.md#series-folders)) |
| Move to series directory | Moves the entries into the matching series folder |
| Empty trashcan | As the red button on level 2 |
| Delete cover | Removes the cover file and cache entry of the entries |
| Bookmarks | Edit the scanned directories |
| Archive | Only shown when *Enable archive* is on |
| Reload cache | Rescan |
| Remove all marks | Deletes the cut-list marks of the entries (not the resume position) |
| Setup | Settings |
| About | Version and licence |

## While playing

| Key | Action |
|---|---|
| **OK** | Show or hide the info bar; while paused, resume |
| **PLAY** | Play / pause |
| **STOP**, **EXIT**, **POWER** | Stop playback and return to the list (the position is saved) |
| **CHANNEL+** | Skip forward (smart jump) |
| **CHANNEL-** | Skip backward (smart jump) |
| **INFO** | EPG info of the recording |
| **FAST FORWARD**, **REWIND**, pause, slow motion | Standard Enigma2 trick play |
| Audio and subtitle keys | Standard Enigma2 audio and subtitle selection |

Smart jump is explained in [Playback](Playback.md#smart-jump).
