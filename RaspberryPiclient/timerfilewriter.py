import time
import urllib
import pickle





def waitasec():
    time.sleep(2.0)





 
#server url
serverapi = "https://radiant-taiga-9466.herokuapp.com/api/status"
#serverapi = "http://localhost:5000/api/status"

while (1):
	try: 
		f = urllib.urlopen(serverapi)   
		dictstatus = f.readline()  

		file = open('status.txt', 'w')
		pickle.dump(dictstatus, file)
		file.close()
	except:
		print("ongelma")   
	waitasec()







	
