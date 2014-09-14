#!/usr/bin/python
##################################################################
#Network-Scout - An Addition to Artillery
#An artillery logging and web interface
#By Shawn Jordan and Aedan Somerville
#Special thanks to Dave Kennedy, DOW Chemical Co., Marshall University
#Adafruit, Jusbour and the Open Source Community
########################## GO HERD ###############################
##################################################################

import time, os, subprocess, re
from Adafruit_CharLCD import Adafruit_CharLCD
import RPi.GPIO as GPIO

lcd = Adafruit_CharLCD()
lcd.begin(16,1)
message = ' '

#Discovers if artillery is running
def artillery_status():
	proc = subprocess.Popen("ps aux | grep artillery.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	stdout = proc.communicate()

	try:
		for line in stdout:
			match = re.search("python /var/artillery/artillery.py", line) or re.search("python nsserver.py", line)
				
			if match:
				message = 'Artillery...Okay\n'
				return message
			else:
				message = "Artillery...Down\n"
				return message
			
	except Exception:
		message = "Artillery..Error\n"
		return message

#Discovers if Network-Scout Server is running
def nsserver_status():
	proc = subprocess.Popen("ps aux | grep nsserver.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	stdout = proc.communicate()

	try:
							
		for line in stdout:
			match = re.search("/usr/bin/python /var/networkscout/nsserver.py", line) or re.search("python nsserver.py", line)
							
			if match:
				message = 'Server...Okay\n'
				return message
			else:
				message = "Server...Down\n"
				return message
					
	except Exception:
		message = "Server..Error\n"
		return message

#Determines whether to use artillery function or NS function
if os.path.isdir("/var/artillery/"):
	while True:
	
		#setting variables
		message = ""
		cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1" 

		#Function that gets ip address
		def run_cmd(cmd):
			p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
			output = p.communicate()[0]
			return output
		
		#Clears the lcd screen
		lcd.clear()

		#Sets the variables to be seen on the screen
		ipaddr = run_cmd(cmd)
		status = artillery_status()

		#Prints the variables to the screen
		lcd.message( (status) )
		lcd.message('IP %s' % ( ipaddr ) )
		
		#Waits 1 minute to update
		time.sleep(60)
else:		
	while True:
	
		#setting variables
		message = ""
		cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1" 
		
		#Function that gets ip address
		def run_cmd(cmd):
			p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
			output = p.communicate()[0]
			return output

		#Clears the lcd screen	
		lcd.clear()

		#Sets the variables to be seen on the screen
		ipaddr = run_cmd(cmd)
		status = nsserver_status()

		#Prints the variables to the screen
		lcd.message( (status) )
		lcd.message('IP %s' % ( ipaddr ) )
		
		#Waits one minute to update
		time.sleep(60)
		
