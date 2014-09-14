#!/usr/bin/python
##################################################################
#Network-Scout - An Addition to Artillery
#An artillery logging and web interface
#By Shawn Jordan and Aedan Somerville
#Special thanks to Dave Kennedy, DOW Chemical Co., Marshall University
#Adafruit, Jusbour and the Open Source Community
########################## GO HERD ###############################
##################################################################

from source import core
import sys, os, subprocess, socket
import MySQLdb as msdb
#Starting Server side programs

try:
	while True:		
			#(ASSIGN HOST AND PORT VARIABLES (HOST IS LOCAL, PORT IS 514 DESIGNATED BY - 
			#ARTILLERY PORT)
			HOST = ''
			PORT = 514

			#OPEN THE TCP CONNECTION
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.bind((HOST,PORT))
			s.listen(4)
			(conn, (ip, port)) = s.accept()
			data = conn.recv(2024)

			#RECEIVE DATA FROM TCP CONNECTION 
			dfile = open("/var/networkscout/stuff/recievedinfo", "w")
			dfile.write( (data) )
			dfile.close()

			#send back command/message
			conn.send("You're message has been recieved.")
			conn.close()
			s.close()

			log_size = os.stat("/var/networkscout/stuff/recievedinfo").st_size
			if log_size < 1:
				pass
			else:
				#LOOP OVER THE FILE TO READ ALL THE LINES
				of_object = open("/var/networkscout/stuff/recievedinfo", "r")
				loader = file.readlines(of_object)
				of_object.close()
				
				#ASSIGN 0 TO ALL VARIABLES
				clip = []
				ip = ''
				eventtime = ''
				alert = ''
				mess = ''
				flag = 0

				#OPEN DATABASE TO MAKE SERVER CONNECTION
				db = msdb.connect("localhost","root","raspberry","Network_Scout")
				cursor = db.cursor()

				for shell in loader:
					try:
						clip = shell.split(',')
						ip = clip[0]
						eventtime = clip[1]
						alert = clip[2]
						mess = clip[3]
					
                		#PREPARE SQL QUERY TO INSERT A RECORD INTO THE DATABASE
						sql = "INSERT INTO Attacks (rpi_ip,time,alert_level,message)  VALUES (\'" + ip + "\',\'" + eventtime + "\',\'" + alert + "\',\'" + mess + "\');"
						clip[:] = []

						try:
							#EXECUTE THE SQL COMMAND
							cursor.execute(sql)
							#COMMIT YOUR CHANGES IN THE DATABASE
							db.commit()
						except Exception, e:
							#ROLLBACK IN CASE THERE IS AN ERROR     
							db.rollback()
							print("Error: " + format(e))
							print("Database was rolled back...")
							flag=1
							pass
					except:
						pass
							
            	#DISCONNECT FROM SERVER
				db.close()
				
				#checks to ensure all data is in database
				if flag is 1:
					pass
				else:
					#cleans file when all information is stored in MySQL
					cleanfile=open('/var/networkscout/stuff/recievedinfo','w')
					cleanfile.write(' ')
					cleanfile.close()


except sys.excepthook, e:
	print("Network-Scout had an issue... " + format(e))
	pass

except KeyboardInterrupt:
	print("Wibbly Wobbly Timey Wimey...Stuff")
	sys.exit()

except Exception, e:
	print("Network-Scout had an issue... " + format(e))
	pass
