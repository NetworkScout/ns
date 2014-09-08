
#!/usr/bin/python

import MySQLdb as mdb
import sys
import getpass

pword = getpass.getpass("Enter your MySQL password for root:")
cnx = mdb.connect('localhost','root',pword)

with cnx:
        try:
                cur = cnx.cursor()
                cur.execute ("CREATE DATABASE Network_Scout;")
                cur.execute("USE Network_Scout;")
                cur.execute("CREATE TABLE Attacks(incident_number INT PRIMARY KEY NOT NULL AUTO_INCREMENT , rpi_ip VARCHAR(16), time VARCHAR(30) NOT NULL, alert_level VARCHAR(20) NOT NULL, message VARCHAR(200) NOT NULL);")
        except mdb.Error, e:
                cnx.rollback()
                print "Error %d: %s" % (e.args[0],e.args[1])
                sys.exit(1)

cnx.close()