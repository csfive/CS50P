# Tomato Clock

#### Video Demo: 👀

#### Description:

A simple command-line Pomodoro timer.

- Default mode: 25 minutes of focused work followed by a 5‑minute break.
- Custom durations: Use -t <minutes> for a work timer or -b <minutes> for a break timer.
- Visual progress bar: Shows remaining time and completion percentage.
- Desktop notifications: Sends a system alert (Linux with notify-send) when a session ends.
- Keyboard interrupt: Press Ctrl+C to exit gracefully.

Example usage:

```sh
python tomato.py            # 25 min work + 5 min break
python tomato.py -t 15      # 15 min work timer
python tomato.py -b 10      # 10 min break timer
python tomato.py -h         # show help
```
