import time
import urllib
import pickle
import json


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
#serverurlstatus = "https://radiant-taiga-9466.herokuapp.com/status"
#serverurltime = "https://radiant-taiga-9466.herokuapp.com/time"


# measure process time
timeriasetus = 5.0/10000
t0 = time.clock()
t1 = t0 + timeriasetus







while (1):

	pklpfile = open("status.txt")
	loaded_data = pickle.load(pklpfile)
	deserialized_data = json.loads(loaded_data)
	pklpfile.close()
	isrunning = deserialized_data["status"]
#	timeleft= dict[3]

#	changedate = dict[4]
		
	while (isrunning == 2):
		pklpfile = open("status.txt")
		loaded_data = pickle.load(pklpfile)
		deserialized_data = json.loads(loaded_data)
		pklpfile.close()
		isrunning = int(deserialized_data["status"])
		timeleft = deserialized_data["timeleft"]    
		changedate = deserialized_data["changedate"]   
		prevchangedate = changedate
		changetime = time.clock()
		timeleft = int(timeleft)
		timeleftnow = timeleft
		duetime = int(time.time()) + timeleft

		while (changedate == prevchangedate) and (isrunning == 2):
			processtime = time.time()
 		
			pklpfile = open("status.txt")
			loaded_data = pickle.load(pklpfile)
			deserialized_data = json.loads(loaded_data)
			pklpfile.close()
			changedate = deserialized_data["changedate"]  

			timeleftnow = duetime - time.time()
			
			timeleftnow = int(timeleftnow)     
			if (timeleftnow < 0):
				timeleftnow ==0
		
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
			print kokominuutit +':' +kokosekunnit	

			processtime = time.time() - processtime
			time.sleep(1.0-processtime)
		
						

		


	while (isrunning == 1):
			gettimertime()
		 	waitasec()
		 	pklpfile = open("status.txt")
			loaded_data = pickle.load(pklpfile)
			deserialized_data = json.loads(loaded_data)
			pklpfile.close()
			isrunning = int(deserialized_data["status"])
			timeleft = deserialized_data["time"]    
			changedate = deserialized_data["changedate"]   
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


	while (isrunning == 0):
		pklpfile = open("status.txt")
		loaded_data = pickle.load(pklpfile)
		deserialized_data = json.loads(loaded_data)
		pklpfile.close()
		isrunning = int(deserialized_data["status"])
		timeleft = deserialized_data["timeleft"]    
		changedate = deserialized_data["changedate"]   

	 	dt = list(time.localtime())
	 	hour = dt[3]
	 	minute = dt[4]
	 	second = dt[5]
	 	print "Aika: %d : %d : %d" % (hour, minute, second) 
	 	waitasec()
		


	
