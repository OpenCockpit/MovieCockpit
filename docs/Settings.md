# Settings

Open the settings with **Open setup** (blue, level 4) or **Setup** in the function menu. Each entry has a short
description at the bottom of the screen. The *Log level* entry is only shown in expert mode.

## List

| Setting | Default | Effect |
|---|---|---|
| Show bookmark content on start | on | The list opens in the home directory. Off: it opens where you left it (the home directory if that is not reachable any more) |
| Default sort mode | Date sort down | Sort mode for folders that have none of their own |
| Show directories information | `(#/GB)` | What the date column shows for folders: off, *Description*, count `(#)`, count and size `(#/GB)`, size `(GB)` |
| Show mount points | off | Show the disk name instead of the date in the date column. The same switch as **Date / Mount** |
| Watching in progress percent | 10 | From this percent watched the icon shows *watching* (0-30) |
| Finished watching percent | 90 | From this percent watched the icon shows *finished* (50-100) |
| Preferred EPG language | UI language | Language used for event names and descriptions when an EIT file contains several |

Not in the setup screen, but stored in the settings file (`/etc/enigma2/settings`). To change one, stop Enigma2
first, edit the file, and start Enigma2 again:

| Key | Default | Effect |
|---|---|---|
| `config.plugins.moviecockpit.movie_date_format` | `%d.%m.%Y %H:%M` | Layout of the date column, see below |
| `config.plugins.moviecockpit.movie_description_delay` | 200 | Milliseconds the cursor must rest before the details pane updates |
| `config.plugins.moviecockpit.piconspath` | `/usr/share/enigma2/picon` | Picon directory |

The *list content* mode (FF/REW) is stored as `config.plugins.moviecockpit.list_content`.

## Colours

| Setting | Default |
|---|---|
| Default color for video | grey |
| Default color for highlighted video | white |
| Default color for recording | red |
| Default color for highlighted recording | light red |
| Default color for selected video | dark yellow |
| Default color for highlighted selected video | yellow |

Video colours come from white, light grey, grey, dark grey and black. Recording colours: red, light red, dark red.
Selection colours: dark yellow, yellow or any video colour. "Highlighted" is the row under the cursor.

## Date format

`movie_date_format` is a Python `strftime` format. The values the plugin knows are:

| Value | Shows as |
|---|---|
| `%d.%m.%Y` | DD.MM.YYYY |
| `%a %d.%m.%Y` | WD DD.MM.YYYY |
| `%d.%m.%Y %H:%M` | DD.MM.YYYY HH:MM (default) |
| `%a %d.%m.%Y %H:%M` | WD DD.MM.YYYY HH:MM |
| `%d.%m. %H:%M` | DD.MM. HH:MM |
| `%a %d.%m. %H:%M` | WD DD.MM. HH:MM |
| `%Y/%m/%d` | YYYY/MM/DD |
| `%a %Y/%m/%d` | WD YYYY/MM/DD |
| `%Y/%m/%d %H:%M` | YYYY/MM/DD HH:MM |
| `%a %Y/%m/%d %H:%M` | WD YYYY/MM/DD HH:MM |
| `%m/%d %H:%M` | MM/DD HH:MM |
| `%a %m/%d %H:%M` | WD MM/DD HH:MM |

(WD is the abbreviated weekday.) Use one of these values; other strings are not accepted by the setting.

## Playback

| Setting | Default | Effect |
|---|---|---|
| Resume video at last position | on | Offer to continue at the saved position, see [Playback](Playback.md) |
| Video start at | event start | *beginning*, *first mark* or *event start* |

## Covers

| Setting | Default | Effect |
|---|---|---|
| Cover source | TVSpielfilm | Where to download from. *automatic* tries the sources in turn. Needs CoverCockpit |
| Show fallback cover | on | Show a placeholder when there is no cover |
| Download cover automatically for recording | on | Request a cover from CoverCockpit whenever a recording starts. Off: only covers you place yourself are shown |

## Trashcan

| Setting | Default | Effect |
|---|---|---|
| Show trashcan directory | on | Show the `.Trash` row in the home directory |
| Show trashcan information | `(#/GB)` | Count and size next to the trashcan row |
| Enable auto trashcan cleanup | on | Empty the trashcan automatically when the box is shut down (needs PowerCockpit). Off: only **Empty trashcan** empties it |
| File retention period in trashcan | 3 days | Files older than this are removed by the clean-up at shutdown (0-30) |

## Archive

| Setting | Default | Effect |
|---|---|---|
| Enable archive | off | Shows the **Archive** function (colour button and menu) and lets the shutdown archive (needs PowerCockpit). Off: nothing is archived |
| Archive source | `/media/hdd/movie` | Recordings below this directory are archived |
| Archive target | `/media/hdd/movie` | Where they go. Must differ from the source |

See [Managing Recordings](Managing-Recordings.md#archive).

## Cache

| Setting | Default | Effect |
|---|---|---|
| Cache directory | `/etc/enigma2` | Folder that holds `moviecockpit.db`. Put it on a disk that is always there |
| Log level | INFO | `ERROR`, `INFO` or `DEBUG` for the log lines that start with `MVC:` (expert) |

See [Cache Database](Cache-Database.md).

## Timers

| Setting | Default | Effect |
|---|---|---|
| Automatic cleanup of timers list | off | Remove finished recording timers from the timer list when Enigma2 starts and two seconds after each recording ends |
