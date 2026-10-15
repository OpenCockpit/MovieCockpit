# Skinning

This page is for people who want to change how MovieCockpit looks, or who are writing a skin that includes it.

## How the skin is built

MovieCockpit brings its own skin. It is written in **YAML** and compiled to the XML that Enigma2 reads:

```
src/skin/default/
    skin.yml                        list of included parts
    screen_MovieCockpit.ymlinc      the main list screen
    screen_MovieCockpitSummary.ymlinc   the front-panel display (LCD / OLED)
    screen_MovieInfoEPG.ymlinc      the info screen
    screen_RecordingInfo.ymlinc     the technical info screen
    screenpart_MovieList.ymlinc     the list widget (rows)
    screenpart_MovieDetails.ymlinc  the right-hand details pane
    skin.xml                        the compiled result, loaded by the plugin
src/skin/images/                    icons used by the screens
```

The plugin loads `skin.xml` from its own directory when it starts, and again whenever the skin is changed
(`WHERE_SKINCHANGE`). Edit the `.ymlinc` files and rebuild `skin.xml`; do not edit `skin.xml` by hand.

`skin.yml` also pulls in shared parts and screens that belong to other Cockpit plugins: the title bar and footer,
the global colours, fonts and sizes, the **player screens** (`CockpitPlayer`, `CockpitPlayerSummary`,
`ScreenPVRState`, `BufferingProgress`) and `FileManagerProgress`. Changing those changes every Cockpit plugin.

Sizes and fonts are written with variables (`$FR_medium`, `$screen_height-55`, ...) that the global parts define, so a
skin can restyle everything by redefining them.

## Screens

| Screen name | Size | Purpose |
|---|---|---|
| `MovieCockpit` | 1920 x 1080 | The list |
| `MovieCockpitSummary` | 396 x 240 | Front-panel display while the list is open |
| `MovieInfoEPG` | 1200 x 820 | Programme info (INFO key) |
| `RecordingInfo` | 1920 x 1080 | Technical info (key 5) |

### Widgets on the `MovieCockpit` screen

| Widget / source | Content |
|---|---|
| `list` (source, rendered by `Listbox` with the `COCTemplatedMultiContentEx` converter) | The rows |
| `Service` (source `COCServiceEvent`) | The event of the entry under the cursor, for the details pane |
| `DiskSpace` (source `COCDiskSpace`, converter `COCDiskSpaceInfo`, text `SpaceInfo`) | `hdd: 42.5%, nas: 61.0%` |
| `sort_mode` (label) | Name of the current sort mode |
| `level` (label) | `<1>` ... `<4>`, the colour-button level |
| `key_red`, `key_green`, `key_yellow`, `key_blue` (buttons) | Labels of the colour buttons at the current level |
| `key_menu`, `key_info` (buttons) | Fixed labels |
| `pic_loading` (widget) | Spinner while the list loads |

The details pane uses these converters on the `Service` source: renderer `COCCover` for the picture; converter
`COCEventName` with `Name`, `Description` and `ShortAndExtendedDescription`; `ServiceTime` with `Duration`;
renderer `COCRunningText` for the scrolling description. They come from **ComponentsCockpit**.

## The list row

The list source delivers one tuple per row. The first 20 entries are the database columns, followed by
nine values that MovieCockpit computes for display:

| Index | Content |
|---|---|
| 0 | type (1 file, 2 folder, 3 link) |
| 1 | bookmark |
| 2 | path |
| 3 | path relative to the bookmark |
| 4 | folder |
| 5 | relative folder |
| 6 | file name |
| 7 | extension |
| 8 | title (name as stored) |
| 9 | programme start time (epoch seconds) |
| 10, 11 | recording start, stop time |
| 12 | length in seconds |
| 13 | short description |
| 14 | extended description |
| 15 | service reference |
| 16 | size in bytes |
| 17 | cut list (pickled) |
| 18 | sort mode |
| 19 | host name |
| **20** | **display name** (the trashcan name is translated) |
| **21** | **date column text** (date, folder info, disk name or the running operation) |
| **22** | **progress**, normal entries only |
| **23** | **icon** (folder, back, link, trashcan, movie in its state) |
| **24** | **picon** |
| **25** | **text colour** |
| **26** | **text colour, highlighted** |
| **27** | **progress**, running recordings only |
| **28** | **progress**, marked entries only |

The default skin draws, from left to right: icon (23), picon (24), title (20, colours 25/26), then the three progress
bars on the same spot, then the date text (21). The progress fields refer to the index as a negative number
(`-22`, `-27`, `-28`).

Why three progress bars? A progress bar's colour cannot be changed per row, so each state has its own bar with its own
fixed colour (grey, red, yellow). For each row only one of them carries a percentage; the other two hold `-1`, which
makes the list skip them. The rule for which one is the same as for the text colour: marked (or busy) first, then
running recording, then normal. For folders and links all three are `-1`, so no bar is drawn.

> If you add or remove columns, the indices used in the skin must follow. They are written as plain numbers in the
> skin because a skin cannot see the constants in `MovieList.py` (`ROW_IDX_*`). Keep both in sync.

## Icons

The icons are read from the plugin's own `skin/images/` directory, installed with the plugin (the files come from the
shared set of the Cockpit plugins). The list uses `back.svg`, `dir.svg`, `link.svg`, `movie_default.svg`,
`movie_watching.svg`, `movie_finished.svg`, `movie_rec.svg`, `bookmark.svg`, `trashcan.svg` and `deleted.svg`, and
`no_cover.png` for the fallback cover. The header uses `sort.svg` and `hardisk.svg`. The player shows
`dvr_controls/*.svg` for play, pause, forward, backward and stop, and `player.svg` as its corner icon.

## Colours and the settings

The six text colours in the [settings](Settings.md#colours) are given to the converter as the row values 25 and 26, so
they work with any row template that uses `MultiContentTemplateColor` with those indices, as the default does. A skin
that draws its own colours simply ignores them.

## The front-panel display

`MovieCockpitSummary` shows the title of the current entry (source `parent.Service`, converter `ServiceName`), and the
file size and the movie duration via the `COCMovieInfo` converter (`FileSize`, `MovieDuration`).
