# Covers and Metadata

## Where the information comes from

For a normal Enigma2 recording (`.ts`) MovieCockpit reads the files that sit next to it:

| File | Holds | Used for |
|---|---|---|
| `Title.eit` | The EPG event as received from the broadcaster | Title, short and extended description, exact start time and length of the **programme** |
| `Title.ts.meta` | Enigma2's recording meta data | Service reference, name, description, recording start/stop time; used when there is no EIT |
| `Title.ts.xmeta` | MovieCockpit's own additions: when the recording really started and stopped, the margins that were used | Trimming the margins off the length |
| `Title.ts.cuts` | Cut list: marks, in/out points, the last watched position | Resume position, progress bar, *first mark* start |
| `Title.txt` | Optional text you wrote | Replaces the extended description |
| `Title.jpg` | Cover | The picture shown for the entry |

If a recording has neither an EIT nor a meta file, the title is built from the file name (the usual
`YYYYMMDD HHMM - Channel - Title` pattern) and the length is unknown.

### Exact event times

An Enigma2 recording normally starts a few minutes early and ends a few minutes late. MovieCockpit combines the EIT
(programme start and length) with the real recording start and stop it has stored, and shows the **programme** start
and length, clipped to what was really recorded. If the recording started in the middle of the programme, the
start shown is where the recording starts; if it was cut off early, the length is shortened accordingly.

The same start time is what *Video start at: event start* uses to skip the pre-roll when you play the recording
(see [Playback](Playback.md)).

> **Tip:** if a time or length looks wrong, select the entry and press **5** (Recording Info). It lists the values from
> the cache, the EIT file, the meta file and the xmeta file side by side. See [Troubleshooting](Troubleshooting.md).

### Recordings split into parts

Recordings that Enigma2 splits into numbered parts (`Title_001.ts`, `Title_002.ts`) are listed as separate entries
named `Title (001)`, `Title (002)`. They share the cover of the base name.

### Other video files

Files that are not recordings (for example `.mkv` or `.mp4`) are listed too. Their length comes from `ffprobe`. If a
`.meta` file exists, its name, description, service and date are used; otherwise the date is the file's creation time.
They get a service reference matching their type so that they play.

### Folders

A folder's description comes from a text file named after the folder (`Series.txt` beside the folder `Series`).
The folder date is its modification time. The `..` row and the trashcan row have no description.

## Covers

### What counts as a cover

A cover is a JPEG file with the **same base name as the recording**:

```
Movie Title.ts
Movie Title.jpg       <- cover of this recording
```

A **folder** cover is a JPEG named after the folder, either next to it or inside it:

```
Series/                 the folder
Series.jpg              <- cover of the folder (next to it)
Series/Series.jpg       <- also accepted (inside it)
```

You can place covers by hand. They are read into the cache the next time the entry is loaded or the cache is
reloaded (see [Cache Database](Cache-Database.md)).

### Which cover is shown

For an entry MovieCockpit looks for:

1. a cover of the entry itself (for a numbered part, of the base name without the `_001`),
2. otherwise a cover of the **folder** it is in,
3. otherwise a built-in "no cover" picture, if *Show fallback cover* is on (default).

This is why a series folder with one cover gives every episode in it a picture.

### Downloading covers

Covers are downloaded by the optional **CoverCockpit** plugin, not by MovieCockpit itself. When a recording
starts and *Download cover automatically for recording* is on (default), CacheCockpit asks CoverCockpit for a cover
for that programme; the picture is saved as `<recording>.jpg` and the entry is refreshed. Without CoverCockpit, or
with the setting off, nothing is downloaded and only covers you place by hand are shown.

*Cover source* (Settings) chooses where to look:

| Source | Meaning |
|---|---|
| TVSpielfilm (default) | Look only at TVSpielfilm |
| TVMovie | Look only at TVMovie |
| HÖRZU | Look only at HÖRZU |
| TV Für Alle | Look only at TV Für Alle |
| automatic | Try the sources in CoverCockpit's own priority order until one returns a picture |

The channel of a recording is matched to the source's channel list by its service reference
(CoverCockpit ships a channel table). Channels that are not in the table get no automatic cover.

Delete a cover that you do not like with **Delete cover** in the function menu. It removes the JPEG file and the cached
picture. For a folder it removes the folder cover.

## Movie info and downloads

| Where | Plugin | What you get |
|---|---|---|
| **INFO** (short) | built in | Programme information from the cache (EPG info) |
| **INFO** (long), or **yellow** in the EPG info | TMDBCockpit | Information and artwork from The Movie Database. When it changes files for the entry, the entry is reloaded into the cache |
| **blue** in the EPG info | MediathekCockpit | Search the German public-service Mediatheken for the title and download it |

These buttons are only shown when the corresponding plugin is installed.
