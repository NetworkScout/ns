#Core code - Special thanks to Adafruit for help with the LCD Code and Malbury Circuits for the simple button script!
#IMPORT LIBRARIES
import time, os, subprocess, re, sys, socket

#Code from project artillery
def kill_artillery():
	print "[*] Checking to see if Artillery is currently running..."
	proc = subprocess.Popen("ps au | grep /var/artillery/artillery.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	stdout = proc.communicate()
	try:
		for line in stdout:
			match = re.search("python /var/artillery/artillery.py", line) or re.search("python artillery.py", line)
			if match:
				print "[*] Killing running version of Artillery.."
				line = line.split(" ")
				pid = line[6]
				subprocess.Popen("kill %s" % (pid), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
				print "[*] Killed the Artillery process: " + pid
	except: pass



#This function will search the file and find the line
def modify_program(lookup,file_name,inserted):
	linenum = 0
	
	with open(file_name) as file:
		for num, line in enumerate(file):
			if lookup in line:
				linenum = num
	
	f = open(file_name, "r")
	contents = f.readlines()
	f.close()
	
	line_num = linenum+1
	contents.insert(line_num, inserted)

	f = open(file_name, "w")
	contents = "".join(contents)
	f.write(contents)
	f.close()

#Modded code from project artillery
def kill_ns_server():
	print "[*] Checking to see if Network Scout is currently running..."
	proc = subprocess.Popen("ps au | grep /var/networkscout/nsserver.py", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	stdout = proc.communicate()
	try:
		for line in stdout:
			match = re.search("ps -au | grep /var/networkscout/nsserver.py", line) or re.search("python nsserver.py", line)
			if match:
				print "[*] Killing running version of Network Scout..."
				line = line.split(" ")
				pid = line[6]
				subprocess.Popen("kill %s" % (pid), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
				print "[*] Killed the Network Scout process: " + pid
	except: pass
	
def send_log_to_server(log_path,server):
	#creating a socket and connecting
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(( (server), 514))
	#opening log to send to server
	file = open(log_path, 'r')
	contents = file.read()
	file.close()
	#sending and closing connection
	s.send( (contents) )
	data = s.recv(2048)
	s.close()
	return
	
def get_config_path():
    path = ""
    if os.path.isfile("/var/networkscout/config"):
        path = "/var/networkscout/config"
    if os.path.isfile("config"):
		path = "config"
    return path

def read_config(param):
    path = get_config_path()
    fileopen = file(path, "r")
    for line in fileopen:
        if not line.startswith("#"):
            match = re.search(param + "=", line)
            if match:
                line = line.rstrip()
                line = line.replace('"', "")
                line = line.split("=")
                fileopen.close()
                return line[1]
                
def ipgrab():
    cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
    output = p.communicate()[0]
    output = output.strip()
    return output
                
