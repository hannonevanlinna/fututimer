import time
import urllib2
import pickle
from shutil import copyfile



 
#server url
serverapi = "https://radiant-taiga-9466.herokuapp.com/api/status"
#serverapi = "http://localhost:5000/api/status"
dictstatus = '{"status":0,"time":"3600","timeleft":"0","message":"","changedate":"2016-02-01T16:44:20.153Z"}'


while (1):
	try: 
		f = urllib2.urlopen(serverapi, timeout=5.0)   
                dictstatus = f.readline()
	except: 
		print("network issues")
	else:
		if ( len(dictstatus)>10):	
			try: 
				file = open('statusr.txt', 'w')
				pickle.dump(dictstatus, file)
				file.close()
			except:
				print("ongelma")
			else: 
				copyfile('statusr.txt', 'status.txt')   
	time.sleep(2.0)







	
