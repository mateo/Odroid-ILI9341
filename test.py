# This script tests the fully wired up LCD using SPI
# Must be run as sudo

import board
import digitalio
import busio

import adafruit_rgb_display.ili9341 as ili9341

from PIL import Image, ImageDraw

cs_pin = digitalio.DigitalInOut(board.D15)		# USES THE SHIFTER SHIELD LAYOUT
dc_pin = digitalio.DigitalInOut(board.D13)
reset_pin = digitalio.DigitalInOut(board.D7)

BAUDRATE = 24000000	# Not sure about this

spi = busio.SPI(clock=board.SCLK, MOSI=board.MOSI, MISO=board.MISO)

disp = ili9341.ILI9341(
    spi,
    rotation=90,	# Not sure about this
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)

if disp.rotation % 180 == 90:
    height = disp.width
    width = disp.height
else:
    width = disp.width
    height = disp.height

image = Image.new("RGB", (width, height))

draw = ImageDraw.Draw(image)

# Blue Screen Test
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 255))
disp.image(image)