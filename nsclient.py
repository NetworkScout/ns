#!/usr/bin/python
##################################################################
#Network Scout - An Addition to Artillery
#An artillery logging and web interface
#By Shawn Jordan and Aedan Somerville
#Special thanks to Dave Kennedy, DOW Chemical Co.
#Adafruit, Jusbour and the Open Source Community
########################## GO HERD ###############################
##################################################################

#!/usr/bin/python
from source import core
import sys, os, subprocess, time

#Starting Client side programs

server = core.read_config("IP_SERVER_ADDRESS")

# check if its installed (from Artillery)
if not os.path.isfile("/var/networkscout/nsclient.py"):
    print "[*] Network Scout is not installed, running setup.py.."
    subprocess.Popen("python network_scout_setup.py", shell=True).wait()
    sys.exit()

else:
	while True:
		log_size = os.stat("/var/artillery/log/logs.txt").st_size
		if log_size < 10:
			pass
		else:
			try:
				#Function sends the information to the server defined in the CONFIG file
				core.send_log_to_server("/var/artillery/log/logs.txt", (server) )
				
				#Clears data from log once the data has been sent
				art_log = open("/var/artillery/log/logs.txt",'w')
				art_log.write(" ")
				art_log.close()
				
			except Exception, e:
				print("Network scout had an issue... " + format(e))
				pass
			except sys.excepthook, e:
				print("Network scout had an issue... " + format(e))
				pass
		
		#Waits 1 minute to check log again
		time.sleep(60)
	
