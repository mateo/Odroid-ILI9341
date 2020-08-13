# Scripts for using an ILI9341 LCD with an Odroid XU4 in Python
Look this isn't fancy.  I was having a lot of trouble getting the Odroid XU4 to work with [this Adafruit SPI LCD](https://www.adafruit.com/product/1770).  After messing around with some libraries, opening a ticket, and getting to the bottom of the issues, here's an install script that sets the Odroid up for use and a test script that makes sure everything is working.

## Libraries
The main libraries at work here are [libgpiod](https://kernel.googlesource.com/pub/scm/libs/libgpiod/libgpiod), [Adafruit Blinka](https://pypi.org/project/Adafruit-Blinka/) and [Adafruit CircuitPython](https://github.com/adafruit/circuitpython) (more specifically, [adafruit/Adafruit_CircuitPython_RGB_Display](https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display))

## Usage
First use the setup script to initialize SPI and install all the libraries:
```
sudo chmod a+x setup.sh
./setup.sh
```

After this, a good test to make sure everything works is to run `sudo python3`
```python
>>> import board
>>> dir(board)
```
The output should be an oject containing a list of Adafruit named pinouts, most starting with D and some SPI and I2C specific ones.

Then run the test script
`sudo python3 test.py`

If you are using another CircuitPython Compatible Display this test script should work, just adapt it through the guide linked below

## Pin Numberings
The software pin numberings used here are defined as part of Adafruit Blinka.  The pin numberings are based on the Shifter Shield physical pinout (Pin D7 is the 7th physical pin).  The shifter shield is required to use this LCD as the SPI bus requires at minimum 3.3v logic, but if you plan to use the GPIO pins for other purposes at 1.8v, check the [schematic for the shifter shield](https://dn.odroid.com/homebackup/XU4_SHIFTER_SHIELD_REV0.1.pdf) to figure out the Adafruit pin numberings, or use this handy chart I made because I love you kind stranger

| Adafruit Pin | GPIO Physical Pin | Odroid GPIO Pin | WiringPi Pin |
|-----|----|----|----|
| D7  | 15 | 18 | 7  |
| D13 | 13 | 21 | 2  |
| D15 | 17 | 22 | 3  |
| D16 | 18 | 19 | 4  |
| D18 | 25 | 23 | 5  |
| D22 | 26 | 24 | 6  |
| D26 | 24 | 25 | 11 |
| D29 | 20 | 28 | 21 |
| D31 | 19 | 30 | 22 |
| D32 | 21 | 29 | 26 |
| D33 | 22 | 31 | 23 |
| D36 | 27 | 33 | 27 |

## Final Notes
I do not maintain any of the libraries involved in these scripts nor do I even know that much about them, any questions regarding them should be directed to the creators, however if this script fails to run do let me know, I can try my best to troubleshoot.  If you wish to use this with the same display, or another CircuitPython supported display, check out [this guide](https://learn.adafruit.com/adafruit-2-8-and-3-2-color-tft-touchscreen-breakout-v2/python-usage) from Adafruit but skip any steps regarding dependencies
