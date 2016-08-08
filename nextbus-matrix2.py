# NextBus scrolling marquee display for Adafruit RGB LED matrix (64x32).
# Requires rgbmatrix.so library: github.com/adafruit/rpi-rgb-led-matrix

import atexit
import Image
import ImageDraw
import ImageFont
import math
import os
import time
from predict import predict
from rgbmatrix import Adafruit_RGBmatrix

# Configurable stuff ---------------------------------------------------------


width          = 64  # Matrix size (pixels) -- change for different matrix
height         = 32  # types (incl. tiling).  Other code may need tweaks.
matrix         = Adafruit_RGBmatrix(32, 2) # rows, chain length
fps            = 20  # Scrolling speed (ish)


# presentation pain colors
r 		= 0
g		= 255
b		= 0

#font           = ImageFont.load(os.path.dirname(os.path.realpath(__file__))
#                   + '/helvR08.pil')

font 		= ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 22)

fontYoffset    = -2  # Scoot up a couple lines so descenders aren't cropped

# Main application -----------------------------------------------------------

# Drawing takes place in offscreen buffer to prevent flicker
#image       = Image.new('RGB', (width, height))
#draw        = ImageDraw.Draw(image)
#currentTime = 0.0
#prevTime    = 0.0

# Clear matrix on exit.  Otherwise it's annoying if you need to break and
# fiddle with some code while LEDs are blinding you.
def clearOnExit():
	matrix.Clear()

atexit.register(clearOnExit)


# Initialization done; loop forever ------------------------------------------
while True:

	# Clear background
	draw.rectangle((0, 0, width, height), fill=(0, 0, 0))
        draw.text((3, 3), "18:23", font=font, fill=(r ,g, b))
	r = r +1
	g = g -1
	if(r>255):
		r=0
	if(g<0):
		g=255

	# Try to keep timing uniform-ish; rather than sleeping a fixed time,
	# interval since last frame is calculated, the gap time between this
	# and desired frames/sec determines sleep time...occasionally if busy
	# (e.g. polling server) there'll be no sleep at all.
	currentTime = time.time()
	timeDelta   = (1.0 / fps) - (currentTime - prevTime)
	if(timeDelta > 0.0):
		time.sleep(timeDelta)
	prevTime = currentTime

	# Offscreen buffer is copied to screen
	matrix.SetImage(image.im.id, 0, 0)
