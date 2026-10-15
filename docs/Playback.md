# Playback

Press **OK** on a recording to play it. MovieCockpit uses its own player screen, built on the standard Enigma2
movie player, so audio, subtitles, trick play and the info bar behave as you are used to. This page covers what
is different.

## Where playback starts

When the player has started, MovieCockpit decides where to begin, in this order:

1. **Resume.** If *Resume video at last position* is on (default) and the recording has a saved position, you
   are asked *"Do you want to resume playback at position h:mm:ss?"*. The question times out after
   10 seconds and the default answer is **No**. Answer **Yes** to jump to the saved position.
2. **Otherwise** the *Video start at* setting applies:

| Setting | Playback starts |
|---|---|
| **beginning** | At the very start of the file, including the recording margin before the programme |
| **first mark** | At the first cut-list mark (marks within the first part of the file, shorter than your *margin before* setting, are ignored) |
| **event start** | At the real start of the programme: the recording margin before it is skipped (default) |

*Event start* is what makes a recording that was started a few minutes early begin with the programme and not
with the previous one.

## Progress and resume position

The position is stored when you leave the player (**STOP**, **EXIT** or **POWER**). It is kept in the `.cuts`
file next to the recording (the same file Enigma2 uses for cut marks) and in the cache, so the list can show the
progress bar and the *watching* / *finished* icon without opening the file.

- *Watching in progress percent* (default 10 %) and *Finished watching percent* (default 90 %) decide
  which icon the list shows.
- **Reset progress** (colour button, level 4) clears the saved position of the marked entries.
- **Remove all marks** (function menu) deletes cut-list marks but keeps the saved position.

If you leave the player, MovieCockpit restores the channel you were watching before and refreshes the list
entry.

## Smart jump

The two bouquet keys (**CHANNEL+** / **CHANNEL-**) skip forward and backward. The step is not fixed. It is chosen
so that you home in on the end of a commercial break with a few presses:

| Press | Step |
|---|---|
| The first jump, either direction | **5 minutes** |
| **CHANNEL+** again, right after a forward jump | **1 minute**, and 1 minute for every further press |
| **CHANNEL-** again, right after a backward jump | **5 minutes** again |
| Every time you **change direction** | The step gets shorter: 1 minute, then 30 seconds, then 15 seconds, and stays at 15 seconds |
| No key for 5 seconds | Everything resets; the next jump is 5 minutes again |

Example: a commercial break starts. Press **CHANNEL+** (5 min). You overshoot the end of the break, so press
**CHANNEL-** (back 1 min). Still too far back, so **CHANNEL+** (forward 30 s), then **CHANNEL-** (back 15 s).
After a few presses you are within seconds of the first frame of the film.

Special case: if you are within about a minute of the programme start (the *event start* point, see above), the first
jump is 1 minute instead of 5, so you do not skip past the beginning of the programme.

Jumps never go before the start of the file, and never closer than 5 seconds to the end.

## Playing recordings that are still running

A recording in progress can be played. It is shown in red in the list, and its progress bar shows how much has been
recorded. You cannot move or copy a running recording, and deleting one asks you to stop the recording first.

## Playing from other media

Any video file that Enigma2 can play is listed (see [Cache Database](Cache-Database.md#what-is-scanned)).
Files that are not Enigma2 recordings (no `.eit`/`.meta`) get their length from `ffprobe`, and their date from the
`.meta` file if there is one, otherwise from the file's creation time.
