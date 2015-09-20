#!/usr/bin/python

############################################################################
# Network-Scout - An Addition to Artillery                                 #
 # An artillery logging and web interface                                   #
  # By Shawn Jordan and Aedan Somerville                                     #
   # Special thanks to Dave Kennedy, DOW Chemical Co., Marshall University    #
    # Adafruit, Jusbour and the Open Source Community  						   #
	 # Version 2.0 "THUNDERING HERD"                                            #
################################# GO HERD #######################################
#################################################################################

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#INSTALL ARTILLERY BEFORE INSTALLATION
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#importing necessary modules for setup
import subprocess, re, os, shutil, sys, time
from source import core

answer = ''
option = 0
menuopt = 0
isrpi = ''
ismysql = ''

try:
	###Banners everywhere
	print("Welcome to Network-Scout - An addition logging application for Artillery.")
	print("If you are installing the client side, please download artillery first.\n")

	print(
	"""            *              *                     * \n
            |              /                       /  \n
            |             /                      /  \n
            |            /                      /   \n
_______________+___________+______________________+_____\n
NETWORK SCOUT \n
VERSION: 2.0 "THUNDERING HERD" \n
CREATORS: SHAWN JORDAN AND AEDAN SOMERVILLE \n
UPDATED: SEPTEMBER 1, 2015 \n
	""")

	###This allows us to set up Network Scout for raspberry pi or another system
	print("First, we need to know if you are building a Raspberry Pi version of Network Scout." )
	isrpi = raw_input("Are you using a Raspberry Pi? ")

	##This adds the config option for Pi onto the file
	if answer.lower() == 'y' or answer.lower() == 'yes':
		confile = open("./config", "a")
		confile.write('IS_R_PI="YES"')
		confile.close()
	else:
		confile = open("./config", "a")
		confile.write('IS_R_PI="NO"')
		confile.close()
	print("OPTIONS: \n1. Install Network-Scout Server\n2. Install Network-Scout Client \n3. Uninstall Network Scout \n4. Exit")

	###Menu used for installation of NSServer NSclient and Removal of Network Scout
	menuopt = input("Please select one:    ")

	if menuopt is 1:
		option = 1
		pass
	elif menuopt is 2 and os.path.isdir("/var/artillery/"):
		option = 2
		pass
	elif menuopt is 2:
		print "Please install artillery from github.com/TrustedSec."
		sys.exit()
	elif menuopt is 3 and os.path.isdir("/var/networkscout/"):
		option = 3
		pass
	elif menuopt is 3:
		print "Network-Scout was not detected and could not be uninstalled."
		sys.exit()
	elif menuopt is 4:
		sys.exit()
	else:
		print "Invalid option. Please try again."
		sys.exit()

	if option == 1:
		print "[*]**********  Network server is preparing to install..."
		os.mkdir("/var/networkscout/")
		subprocess.Popen("cp -r ./* /var/networkscout/", shell=True).wait()

		# install to rc.local
		print "[*]********** Adding Network-Scout into startup through init scripts..."
		if os.path.isdir("/etc/init.d"):
			if not os.path.isfile("/etc/init.d/nsserver"):
				fileopen = file("./startup/startup_network_scout_server", "r")
				config = fileopen.read()
				filewrite = file("/etc/init.d/nsserver", "w")
				filewrite.write(config)
				filewrite.close()
				print "[*] Triggering update-rc.d on Network Scout to automatic start..."
				subprocess.Popen("chmod +x /etc/init.d/nsserver", shell=True).wait()
				subprocess.Popen("update-rc.d nsserver defaults", shell=True).wait()



			if isrpi.lower() == 'y' or isrpi.lower() == 'yes':
				print("[*]********** Downloading LAMP Install Script...")
				subprocess.Popen("sudo git clone https://github.com/LikeABoss-001/Raspberry-Pi-LAMP-Install-Script.git", shell=True).wait()
				print "[*]********** INSTALLING LAMP..."
				print"[!]This may take a few minutes. Feel free to get a coffee. [!]"
				subprocess.Popen("sudo chmod +x /home/pi/Raspberry-Pi-LAMP-Install-Script/install.sh && /home/pi/Raspberry-Pi-LAMP-Install-Script/install.sh", shell=True).wait()
				subprocess.Popen("rm -rf Raspberry-Pi-LAMP-Install-Script/",shell=True).wait()
				subprocess.Popen("sudo apt-get install python-rpi.gpio", shell=True).wait()
				print "[*]********** Adding LCD controller into startup through init scripts..."
				subprocess.Popen("sudo apt-get install python-rpi.gpio", shell=True).wait()
				if os.path.isdir("/etc/init.d"):
					if not os.path.isfile("/etc/init.d/lcd_controller"):
						fileopen = file("./ns/startup/lcd_controller", "r")
						config = fileopen.read()
						fileopen.close()
						filewrite = file("/etc/init.d/lcd_controller", "w")
						filewrite.write(config)
						filewrite.close()
						print "[*] Triggering update-rc.d on LCD Controller to automatic start..."
						subprocess.Popen("chmod +x /etc/init.d/lcd_controller", shell=True).wait()
						subprocess.Popen("update-rc.d lcd_controller defaults", shell=True).wait()
				print "[*]********** Adding Shutdown into startup through init scripts..."
				if os.path.isdir("/etc/init.d"):
					if not os.path.isfile("/etc/init.d/shutdown_button"):
						fileopen = file("./ns/startup/shutdown", "r")
						config = fileopen.read()
						fileopen.close()
						filewrite = file("/etc/init.d/shutdown_button", "w")
						filewrite.write(config)
						filewrite.close()
						print "[*] Triggering update-rc.d on Shutdown Button to automatic start..."
						subprocess.Popen("chmod +x /etc/init.d/shutdown_button", shell=True).wait()
						subprocess.Popen("update-rc.d shutdown_button defaults", shell=True).wait()
					subprocess.Popen("chmod 755 /var/networkscout/lcd_controller.py", shell=True).wait()
					subprocess.Popen("chmod 755 /var/networkscout/shutdown.py", shell=True).wait()


				#moving Adafruit into python library
				print("*********************** Putting the Pieces Together ********************")
				subprocess.Popen("cp /var/networkscout/source/Adafruit_CharLCD.py /usr/lib/python2.7/", shell=True).wait()

			else:
				print("We are setting up the website now")
				pass

			subprocess.Popen("chmod 755 /var/networkscout/nsserver.py", shell=True).wait()
			subprocess.Popen("rm /var/networkscout/nsclient.py", shell=True).wait()

			####MAY DISCONTINUE DATABASE USAGE FOR NON-PI Users
			ismysql = raw_input("Will you be using MySQL? (Y/N) *If not, we will use PHP to create the table* ")
			if ismysql.lower() == 'y' or ismysql.lower() == 'yes':
				print("************************** Creating Database for Logs ***********************")
				subprocess.Popen("python /var/networkscout/stuff/mysqltablecreator.py", shell=True).wait()
				if os.path.isdir("/var/www/html/"):
					subprocess.Popen("mv /var/networkscout/website/* /var/www/html/", shell=True).wait()
				else:
					subprocess.Popen("mv /var/networkscout/website/* /var/www/", shell=True).wait()
			else:
				if os.path.isdir("/var/www/html/"):
					subprocess.Popen("mv /var/networkscout/website_phponly/* /var/www/html/", shell=True).wait()
				else:
					subprocess.Popen("mv /var/networkscout/website_phponly/* /var/www/", shell=True).wait()

			serverip = core.ipgrab()
			print("Website created at "+serverip+"/scoutwebsite.php \n")

			answer=raw_input("Do you wish to reboot your pi? [yes|no]    ")
			if answer.lower() == 'y' or answer.lower() == 'yes':
				subprocess.Popen("reboot", shell=True)
			else:
				pass

	elif option == 2:
		print("[*]********** Installing network-scout...")
		core.kill_artillery()
		if os.mkdir("/var/networkscout"):
			subprocess.Popen("cp -r ns/* /var/networkscout/", shell=True).wait()
		elif os.isdir("/var/networkscout"):
			errormes = raw_input("Network scout already exists. Do you want to continue?")
			if errormes.lower() == 'y' or isrpi.lower() == 'yes':
				subprocess.Popen("rm -rf /var/networkscout/", shell=True).wait()
				subprocess.Popen("cp -r ns/* /var/networkscout/", shell=True).wait()
			else:
				pass
		else:
			pass


		#modifying artillery
		print("[*]**********Modding Artillery for NS logging...")
		mod = open("ns/stuff/artilleryfunction", "r")
		contents = mod.read()

		artillery = open("/var/artillery/src/core.py", "a")
		artillery.write(contents)
		artillery.close()
		mod.close()

		#Adding nslog to all parts of artillery

		core.modify_program("warn_the_good_guys","/var/artillery/src/harden.py","	nslog(warning)")
		core.modify_program("warn_the_good_guys","/var/artillery/src/honeypot.py","		    nslog(subject)")
		core.modify_program("warn_the_good_guys","/var/artillery/src/monitor.py","		    nslog(subject)")
		core.modify_program("warn_the_good_guys","/var/artillery/src/ssh_monitor.py","				    nslog(subject)")

		print("[*]********** Creating Log Directory and File...")
		# create the database directories if they aren't there
		if not os.path.isdir("/var/artillery/log/"):
			os.makedirs("/var/artillery/log/")
		if not os.path.isfile("/var/artillery/log/logs.txt"):
			filewrite = file("/var/artillery/log/logs.txt", "w")
        	filewrite.write(" ")
        	filewrite.close()

		# install to rc.local
		print "[*]********** Adding Network-Scout into startup through init scripts..."

		if os.path.isdir("/etc/init.d"):
			if not os.path.isfile("/etc/init.d/nsclient"):
				fileopen = file("./ns/startup/startup_network_scout_client", "r")
				config = fileopen.read()
				fileopen.close()
				filewrite = file("/etc/init.d/nsclient", "w")
				filewrite.write(config)
				filewrite.close()
				print "[*] Triggering update-rc.d on Network Scout to automatic start..."
				subprocess.Popen("chmod +x /etc/init.d/nsclient", shell=True).wait()
				subprocess.Popen("update-rc.d nsclient defaults", shell=True).wait()

		if isrpi.lower() == 'y' or isrpi.lower() == 'yes':

			print "[*]********** Adding LCD controller into startup through init scripts..."
			subprocess.Popen("sudo apt-get install python-rpi.gpio", shell=True).wait()
			if os.path.isdir("/etc/init.d"):
				if not os.path.isfile("/etc/init.d/lcd_controller"):
					fileopen = file("./ns/startup/lcd_controller", "r")
					config = fileopen.read()
					fileopen.close()
					filewrite = file("/etc/init.d/lcd_controller", "w")
					filewrite.write(config)
					filewrite.close()
					print "[*] Triggering update-rc.d on LCD Controller to automatic start..."
					subprocess.Popen("chmod +x /etc/init.d/lcd_controller", shell=True).wait()
					subprocess.Popen("update-rc.d lcd_controller defaults", shell=True).wait()

			print "[*]********** Adding Shutdown into startup through init scripts..."
			if os.path.isdir("/etc/init.d"):
				if not os.path.isfile("/etc/init.d/shutdown_button"):
					fileopen = file("./ns/startup/shutdown", "r")
					config = fileopen.read()
					fileopen.close()
					filewrite = file("/etc/init.d/shutdown_button", "w")
					filewrite.write(config)
					filewrite.close()
					print "[*] Triggering update-rc.d on Shutdown Button to automatic start..."
					subprocess.Popen("chmod +x /etc/init.d/shutdown_button", shell=True).wait()
					subprocess.Popen("update-rc.d shutdown_button defaults", shell=True).wait()

			subprocess.Popen("chmod 755 /var/networkscout/lcd_controller.py", shell=True).wait()
			subprocess.Popen("chmod 755 /var/networkscout/shutdown.py", shell=True).wait()
			subprocess.Popen("cp /var/networkscout/source/Adafruit_CharLCD.py /usr/lib/python2.7/", shell=True).wait()

		else:
			pass

		print("[*]********** Adding access to scripts for init.d...")
		subprocess.Popen("chmod 755 /var/networkscout/nsclient.py", shell=True).wait()
		subprocess.Popen("rm /var/networkscout/nsserver.py", shell=True).wait()

		answer=raw_input("Do you wish to reboot your computer? [yes|no] ")
		if answer.lower() == 'y' or answer.lower() == 'yes':
			subprocess.Popen("reboot", shell=True)
		else:
			pass
	elif option == 3:
		answer = raw_input("Do you want to uninstall network-scout: [ yes | no }    ")
		if answer.lower() == "y" or answer.lower() == "yes":
			subprocess.Popen("rm -rf /var/networkscout", shell=True)
			if os.path.isfile("/etc/init.d/nsclient"):
				os.remove("/etc/init.d/nsclient")
				os.remove("/etc/init.d/lcd_controller")
				os.remove("/etc/init.d/shutdown_button")
			else:
				os.remove("/etc/init.d/nsserver")
				os.remove("/etc/init.d/lcd_controller")
				os.remove("/etc/init.d/shutdown_button")
				subprocess.Popen("python /var/networkscout/stuff/mysqluninstaller.py", shell=True)
				subprocess.Popen("rm /var/www/*", shell=True)
				subprocess.Popen("apt-get purge `dpkg -l | awk -F ' ' ' /php|mysql|otherpackages/ { print $2 } '`", shell=True)

			print "[*] Network-Scout has been uninstalled. Manually kill the process if it is still running."

	else:
		print "There was an issue installing Network-Scout."

except Exception, e:
	print("There was an issue installing network-scout") + format(e)
	sys.exit()
