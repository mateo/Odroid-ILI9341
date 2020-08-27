# This script tests the fully wired up LCD using SPI
# Must be run as sudo

import time

import board
import digitalio
import busio

import adafruit_rgb_display.ili9341 as ili9341

from PIL import Image, ImageDraw, ImageFont

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

font=ImageFont.load_default()

# Image Test
#image = Image.open('logo.bmp').convert('RGB')
#disp.image(image)
#time.sleep(2)
#disp.fill(0)

# Draw Test Setups
image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)

# Blue Screen Test
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 255))
disp.image(image)
time.sleep(2)
disp.fill(0)

# Hello World Test
draw.rectangle((0, 0, width, height), outline=0, fill=(150, 150, 150))
textdraw.text((100,100), "Hello World!", font=font, fill=(255,255,255))
time.sleep(2)
disp.fill(0)

# Look At All Those Chickens!!
draw.rectangle((0, 0, width, height), outline=0, fill=(200, 200, 255))
draw.rectangle((0, 0, width, height/2), outline=0, fill=(0, 200, 0))
draw.rectangle((width/4, height/2, 3*width/4, height/2), outline=0, fill=(255, 175, 75))
for i in range(0,20):
	x = randint(0,width)
	y = randint(0,height/2)
	draw.rectangle((x, y, x+15, y+10), outline=0, fill=(255, 255, 255))
draw.ellipse((-width/3, 0, width/3, height), outline=0, fill=(175, 175, 100))
time.sleep(2)