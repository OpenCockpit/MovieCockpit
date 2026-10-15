# Installation

## Requirements

- An Enigma2 box running OpenViX or a compatible image.
- A Python 3 based image.
- Free space for the cache database (see [Cache Database](Cache-Database.md)); by default it lives in
  `/etc/enigma2`.

## Packages

The package is `enigma2-plugin-extensions-moviecockpit`. It is architecture independent (`all`) and depends on:

| Package | Why |
|---|---|
| `python3-requests`, `python3-six` | Python libraries |
| `enigma2-plugin-skincomponents-componentscockpit` | Skin converters, renderers and sources |
| `enigma2-plugin-systemplugins-mountcockpit` | Bookmarks and mount handling |
| `enigma2-plugin-systemplugins-cachecockpit` | SQL cache and file manager |
| `enigma2-plugin-systemplugins-jobcockpit` | Background jobs for file operations |
| `enigma2-plugin-systemskins-fontcockpit` | Fonts |

CacheCockpit in turn depends on `python3-sqlite3`. The package manager installs and removes these
automatically; there is nothing to install by hand.

### Optional plugins

These are not pulled in by MovieCockpit. Install them if you want the feature:

| Feature | Plugin |
|---|---|
| Cover download | CoverCockpit |
| Movie info (TMDB) from the list | TMDBCockpit |
| Mediathek download from the info screen | MediathekCockpit |
| Trashcan clean-up and archiving at shutdown | PowerCockpit |

## Installing

Install the package with your usual method (feed, `opkg install`, or the plugin installer). When it
finishes it asks you to **restart Enigma2**. The restart is required: MovieCockpit hooks the
PVR / VIDEO key while the session starts.

## First start

1. Press **PVR / VIDEO** in TV mode, or start **MovieCockpit** from the plugin menu.
2. On the very first start the cache database does not exist yet. MovieCockpit waits until the mounts are
   known and then scans every movie directory. A spinner is shown and the list fills as the scan finishes.
   Key **8** opens the file operations progress screen.
3. Later starts reuse the database and open at once.

The bookmarks are taken from Enigma2's own movie directories (`config.movielist.videodirs`) the first time
the plugin runs. Change them afterwards with the **Bookmarks** function (see [Storage and Network](Storage-and-Network.md)).

## Taking over the PVR / VIDEO key

MovieCockpit replaces the movie list of the info bar. It registers with a higher weight than other movie
list plugins, so it also wins when EnhancedMovieCenter or a similar plugin patches the same hook.

## Removing

Remove the package with the package manager. The removal script deletes the plugin directory
`/usr/lib/enigma2/python/Plugins/Extensions/MovieCockpit`. The cache database (`moviecockpit.db`) and your
recordings are not touched. Delete the database by hand if you want it gone.
