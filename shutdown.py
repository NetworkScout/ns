#!/usr/bin/python
##################################################################
#Network Scout - An Addition to Artillery
#An artillery logging and web interface
#By Shawn Jordan and Aedan Somerville
#Special thanks to Dave Kennedy, DOW Chemical Co.
#Adafruit, Jusbour and the Open Source Community
########################## GO HERD ###############################
##################################################################

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP)

cat = True

while cat is True:
    if(GPIO.input(4) == False):
        os.system("sudo shutdown -h now")
        GPIO.cleanup()
        break
    else:
    	time.sleep(1)