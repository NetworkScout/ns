Network Scout
==

Network Scout (NS) is an extension to Artillery. NS allows you to access log files from multiple clients.

Network Scout is a python program, allowing <a href=https://github.com/trustedsec/artillery>artillery</a> to send logs to a centralized server. Network Scout has a pre-built client and server side. Network Scout can easily be set up using the provided setup script.

###
Notes:
Network Scout must be ran from the home directory. To setup NS, do the following:
<ol>
  <li>Download Network Scout</li>
  <li>Type "cd"</li>
  <li>Type "sudo python NS/nssetup.py"</li>
  <li>Follow the instructions</li>
</ol>
Setup script works with server and client sides.

###
Tech Details:

Source contains core functions
Stuff folder holds MySQL scripts, server recieved information and code needed to modify artillery.
Website folder holds the website information until the setup script can move it.
Startup folder has all the init scripts for the following services:
<ul>
  <li>shutdown_button</li>
  <li>lcd_controller</li>
  <li>nsserver (server side only)</li>
  <li>nsclient (server side only)</li>
</ul>
All services have the following functionality [start|stop|restart|status]
