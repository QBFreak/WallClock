# Wall Clock

This project aims to take a Raspberry Pi with an attached display and mount it
to a wall to serve as a lighted clock. Desired functionality includes:

 - Display date and time in as large a font as possible (fill the display)
 - IR Remote control - turn off the backlight for use at night
 - Auto backlight control based on light levels?
 - Adjust clock features via remote

The project is in the early stages and presently is only capable of displaying
the time full-screen, in the largest font that will fit.

## Current functionality

 - Display clock full screen, largest font possible
 - Click/tap anywhere to exit

## Prerequisites

You will need Python 3 (which should be included in the current Raspbian distro)
as well as PyQt5 for Python 3.

```
sudo apt install python3-pyqt5
```

## Testing

To launch Wall Clock from a remote shell (SSH), you must specify the display:

```
$ DISPLAY=0 ./clock.py
```

![WallClock action shot](https://raw.githubusercontent.com/QBFreak/WallClock/raw/master/WallClock.jpg)
