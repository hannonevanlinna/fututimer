# NextBus scrolling marquee display for Adafruit RGB LED matrix (64x32).
# Requires rgbmatrix.so library: github.com/adafruit/rpi-rgb-led-matrix

import atexit
import Image
import ImageDraw
import ImageFont
import math
import os
import time
import urllib
import pickle
import json
#from predict import predict
from rgbmatrix import Adafruit_RGBmatrix

# Configurable stuff ---------------------------------------------------------


width          = 64  # Matrix size (pixels) -- change for different matrix
height         = 32  # types (incl. tiling).  Other code may need tweaks.
matrix         = Adafruit_RGBmatrix(32, 2) # rows, chain length
fps            = 20  # Scrolling speed (ish)

def waitasec():
    time.sleep(1.0)

def gettimertime():
	timerasetus = 5.0/1000
	return


# 0 = timer off
# 1 = timer timer wating for start
# 2 = timer running


# measure process time
timeriasetus = 5.0/10000
t0 = time.clock()
t1 = t0 + timeriasetus





# presentation pain colors
r 		= 0
g		= 255
b		= 0

#fontsmall           = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 10)

fontsmall           = ImageFont.load(os.path.dirname(os.path.realpath(__file__))
                   + '/helvR08.pil')

font 		= ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 25)

fontYoffset    = -2  # Scoot up a couple lines so descenders aren't cropped
xw = 0
# Main application -----------------------------------------------------------

# Drawing takes place in offscreen buffer to prevent flicker
image       = Image.new('RGB', (width, height))
draw        = ImageDraw.Draw(image)
currentTime = 0.0
prevTime    = 0.0

# Clear matrix on exit.  Otherwise it's annoying if you need to break and
# fiddle with some code while LEDs are blinding you.
def clearOnExit():
	matrix.Clear()

atexit.register(clearOnExit)


# Initialization done; loop forever ------------------------------------------
while True:

	# Clear background
	draw.rectangle((0, 0, width, height), fill=(0, 0, 0))

#        try:
#                        with open("status.txt") as json_file:
#                                deserialized_data = json.load(json_file)
 #       except Exception as e:
  #                              print e.__doc__
   #                             print e.message

        try:
                  pklpfile = open("status.txt", "rb")
                  loaded_data = pickle.load(pklpfile)
		  pklpfile.close()	
	except:
                  print("ongelma")
	else: 
	          deserialized_data = json.loads(loaded_data)

	isrunning = deserialized_data["status"]
#	timeleft= dict[3]

#	changedate = dict[4]
		
	while (isrunning == 2):


		try:
                	  pklpfile = open("status.txt", "rb")
                  	  loaded_data = pickle.load(pklpfile)
                  	  pklpfile.close()
        	except:
                	  print("ongelma")
        	else:
                  	  deserialized_data = json.loads(loaded_data)


		isrunning = int(deserialized_data["status"])
		timeleft = deserialized_data["timeleft"]    
		changedate = deserialized_data["changedate"]   
		timertime_full = deserialized_data["time"]
		message = deserialized_data["message"]
                message = message.encode('utf-8')
		prevchangedate = changedate
		changetime = time.clock()
		timeleft = int(timeleft)
		timeleftnow = timeleft
		duetime = int(time.time()) + timeleft

		while (changedate == prevchangedate) and (isrunning == 2):
			processtime = time.time()
 		
			try:
     		                pklpfile = open("status.txt", "rb")
                  		loaded_data = pickle.load(pklpfile)
                  		pklpfile.close()
        		except:
                  		print("ongelma")
        		else:
	                	deserialized_data = json.loads(loaded_data)
	
			changedate = deserialized_data["changedate"]  

			timeleftnow = duetime - time.time()
			
			timeleftnow = int(timeleftnow)     
			if (timeleftnow < 0):
				timeleftnow = 0
		
			minuutit = int(timeleftnow/60)	
			sekunnit = timeleftnow-minuutit*60

			if (minuutit < 10):
				kokominuutit = '0' + str(minuutit)
			else:
				 kokominuutit = str(minuutit)

			if (sekunnit < 10):
				kokosekunnit = '0' + str(sekunnit)
			else:
			 	kokosekunnit = str(sekunnit)
			
			#color according to the phase of the presentation
		
			g = 0.0 + (100*timeleftnow/int(timertime_full))*2.55
			r = 255.0 - (100*timeleftnow/int(timertime_full))*2.55
			g = int(g)
			r = int(r)
		

			textwidth = fontsmall.getsize(message)[0]
                        if (textwidth > 64):
                                xw = xw -1
                        else:
                                 xw = 0
                        if (xw < -textwidth):
                                xw = 64
			if (textwidth > 0):
				voffset = -3
			else:
				 voffset = 2
				

			draw.rectangle((0, 0, width, height), fill=(0, 0, 0))
			draw.text((1, voffset), kokominuutit +':' +kokosekunnit, font=font, fill=(r ,g, b))
        		draw.text((xw, 20), message, font=fontsmall, fill=(0,0,255))
			matrix.SetImage(image.im.id, 0, 0)


			processtime = time.time() - processtime
			time.sleep(0.12 -processtime)
		
						

		


	while (isrunning == 1):
			gettimertime()
		 	time.sleep(0.12)
		 	
			try:
                  		pklpfile = open("status.txt", "rb")
                  		loaded_data = pickle.load(pklpfile)
                  		pklpfile.close()
        		except:
                  		print("ongelma")
        		else:
                  		deserialized_data = json.loads(loaded_data)	
			
			isrunning = int(deserialized_data["status"])
			timeleft = deserialized_data["time"]    
			changedate = deserialized_data["changedate"]
               		message = deserialized_data["message"]
                	message = message.encode('utf-8')   
			timeleft = int(timeleft)
			minuutit = int(timeleft/60)	
			sekunnit = timeleft-minuutit*60

			if (minuutit < 10):
				kokominuutit = '0' + str(minuutit)
			else:
				 kokominuutit = str(minuutit)

			if (sekunnit < 10):
				kokosekunnit = '0' + str(sekunnit)
			else:
				 kokosekunnit = str(sekunnit)
			textwidth = fontsmall.getsize(message)[0]
               		if (textwidth > 64):
                        	xw = xw -1
                	else:
                       		 xw = 0
                	if (xw < -textwidth):
                        	xw = 64
                        if (textwidth > 0):
                                voffset = -3
                        else:
                                 voffset = 2


			draw.rectangle((0, 0, width, height), fill=(0, 0, 0))
                        draw.text((1, voffset), kokominuutit +':' +kokosekunnit, font=font, fill=(r ,g, b))
			draw.text((xw, 20), message, font=fontsmall, fill=(0,0,255))
                        matrix.SetImage(image.im.id, 0, 0)


	while (isrunning == 0):

		try:
                  	pklpfile = open("status.txt", "rb")
                  	loaded_data = pickle.load(pklpfile)
                	pklpfile.close()
        	except:
                  	print("ongelma")
        	else:
                  	deserialized_data = json.loads(loaded_data)

		isrunning = int(deserialized_data["status"])
		timeleft = deserialized_data["timeleft"]    
		changedate = deserialized_data["changedate"]   
		message = deserialized_data["message"]
		message = message.encode('utf-8')	
	 	dt = list(time.localtime())
	 	hour = dt[3]
	 	minute = dt[4]
	 	second = dt[5]
		if (minute < 10):
                     kokominuutit = '0' + str(minute)
                else:
                     kokominuutit = str(minute)

                if (hour < 10):
                     kokohour = '0' + str(hour)
                else:
                     kokohour = str(hour)


		textwidth = fontsmall.getsize(message)[0]		
		if (textwidth > 64):
			xw = xw -1
		else:
			xw = 0
		if (xw < -textwidth):
			xw = 64	
                if (textwidth > 0):
                        voffset = -3
                else:
                        voffset = 2

	 	draw.rectangle((0, 0, width, height), fill=(0, 0, 0))
                draw.text((1, voffset), kokohour +':' +kokominuutit, font=font, fill=(48 ,255, 39))
		draw.text((xw, 20), message, font=fontsmall, fill=(0,0,255))	               
			

		matrix.SetImage(image.im.id, 0, 0)
		time.sleep(0.12)







	# Try to keep timing uniform-ish; rather than sleeping a fixed time,
	# interval since last frame is calculated, the gap time between this
	# and desired frames/sec determines sleep time...occasionally if busy
	# (e.g. polling server) there'll be no sleep at all.
#	currentTime = time.time()
#	timeDelta   = (1.0 / fps) - (currentTime - prevTime)
#	if(timeDelta > 0.0):
#		time.sleep(timeDelta)
#	prevTime = currentTime
#
	# Offscreen buffer is copied to screen
	matrix.SetImage(image.im.id, 0, 0)
