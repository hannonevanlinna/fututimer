import time
import urllib



def waitasec():
    time.sleep(1.0)

def gettimertime():
	timerasetus = 5.0/1000
	return

# 0 = timer off
# 1 = timer timer wating for start
# 2 = timer running


#server url
#serverurlstatus = "http://localhost:5000/status"
#serverurltime = "http://localhost:5000/time"
serverurlstatus = "https://radiant-taiga-9466.herokuapp.com/status"
serverurltime = "https://radiant-taiga-9466.herokuapp.com/time"


# measure process time
timeriasetus = 5.0/10000
t0 = time.clock()
t1 = t0 + timeriasetus







while (1):
	try: 
			f = urllib.urlopen(serverurlstatus)   
			myfile = f.readline()  
			isrunning = int(myfile) 
	except:
		print("ongelma")   

	
	while (isrunning == 2):
		sparetime = time.clock()
 		try: 
 			f = urllib.urlopen(serverurltime)
 			myfile2 = f.readline() 
			timeleft = int(myfile2)
		except:
			sparetime = time.clock() - sparetime
			timeleft = timeleft - sparetime*1000
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
		print kokominuutit +':' +kokosekunnit	

		waitasec()	

		try: 
			f = urllib.urlopen(serverurlstatus)   
			myfile = f.readline()  
			isrunning = int(myfile) 
		except:
			print("ongelma")   


	while (isrunning == 1):
			gettimertime()
		 	waitasec()
			try: 
				f = urllib.urlopen(serverurlstatus)   
				myfile = f.readline()  
				isrunning = int(myfile) 
			except:
				print("ongelma1")   
			
			try: 
				f = urllib.urlopen(serverurltime)           
				myfile2 = f.readline() 
				timeleft = int(myfile2)
			except:
				print("ongelma2")  
					
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
			print kokominuutit +':' +kokosekunnit	


	while (isrunning == 0):
	 	dt = list(time.localtime())
	 	hour = dt[3]
	 	minute = dt[4]
	 	second = dt[5]
	 	print "Aika: %d : %d : %d" %(hour, minute, second) 
	 	waitasec()
		try: 
			f = urllib.urlopen(serverurlstatus)   
			myfile = f.readline()  
			isrunning = int(myfile) 
		except:
			print("ongelma")   


	
