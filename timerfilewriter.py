import time
import urllib
import pickle
from shutil import copyfile



 
#server url
serverapi = "https://radiant-taiga-9466.herokuapp.com/api/status"
#serverapi = "http://localhost:5000/api/status"

while (1):
	try: 
		f = urllib.urlopen(serverapi)   
                dictstatus = f.readline()
	except: 
		print("network issues")
	

	if ( len(dictstatus)>10):	
		try: 
			file = open('statusr.txt', 'w')
			pickle.dump(dictstatus, file)
			file.close()
			copyfile('statusr.txt', 'status.txt')
		except:
			print("ongelma")   
	time.sleep(2.0)







	
