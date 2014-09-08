#!/usr/bin/python

import MySQLdb as mdb
import sys
import getpass

pword = getpass.getpass("Enter your MySQL password for root:")
cnx = mdb.connect('localhost','root',pword)

with cnx:
        try:
                cur = cnx.cursor()
                cur.execute ("DROP DATABASE Network_Scout;")
        except mdb.Error, e:
                cnx.rollback()
                print "Error %d: %s" % (e.args[0],e.args[1])
                sys.exit(1)

cnx.close()