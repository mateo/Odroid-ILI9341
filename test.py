import board
import digitalio
import busio

import adafruit_rgb_display.ili9341 as ili9341

from PIL import Image, ImageDraw

cs_pin = digitalio.DigitalInOut(board.SPI_CS0)
dc_pin = digitalio.DigitalInOut(board.D13)		# Check this is the right format for pins -- python\ dir(board)
reset_pin = digitalio.DigitalInOut(board.D15)	# Check this is the right format for pins -- python\ dir(board)

BAUDRATE = 24000000	# Not sure about this

spi = board.SPI()

disp = ili9341.ILI9341(
    spi,
    rotation=90,	# Not sure about this
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

if disp.rotation % 180 == 90:	# Why not
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height

image = Image.new("RGB", (width, height))

draw = ImageDraw.Draw(image)

# Blue Screen Test
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 255))
disp.image(image)

######## Things to do tomorrow ########
# Initioalize SPI https://wiki.odroid.com/odroid-xu4/application_note/gpio/spi
# Install libgpiod without the header issue https://github.com/aquaticus/nexus433/issues/21
#	Then https://pypi.org/project/gpiod/
# Initialize blinka https://learn.adafruit.com/circuitpython-libaries-linux-odroid-c2/initial-setup
# 	YOU HAVE TO CHANGE THE FILE THAT THROWS AN ERROR< IT READS "Chip" should read "chip"
#	https://github.com/adafruit/Adafruit_Blinka/blob/master/src/adafruit_blinka/microcontroller/generic_linux/libgpiod_pin.py
# Initialize ILI9341 Libraries and pip thingies https://learn.adafruit.com/adafruit-2-8-and-3-2-color-tft-touchscreen-breakout-v2/python-usage
# Other SPI Display Tests