#!/usr/bin/env python

import binascii 
import sys
#import PyQt4 some time in the future..
from os.path import expanduser, splitext

args = sys.argv  
home = expanduser("~")

def hexstr(fn):                # This function makes use of binascii to read file in hex mode
	with open(fn, 'rb') as f:
    		content = f.read()
	Payload = (binascii.hexlify(content))
	return Payload
	
def merger(cov,pld,ext):
	Final = binascii.unhexlify(str(cov)) + "overherelolz" + ext + "extafter"+ binascii.unhexlify(str(pld))
	return Final
	
def usage(reason, ecode):
	print " Usage: " + str(args[0]) + " < hide|get > /file/to/unhide.png\n\n Example: " + str(args[0]) + " hide /path/to/MySecretMessage.txt /some/funny.gif\n"
	print reason + "\n"
	sys.exit(ecode)
	
	
if len(args) >= 3 and len(args) <= 4:
	
	if args[1] == "hide":
		Cover = hexstr(args[3])
		ExtCov = splitext(args[3])[1]
		ExtPay = splitext(args[2])[1]
		Payload = hexstr(args[2])
		destfile = home +"/Desktop/Changedfile" + ExtCov

		print "writting" + destfile 
		file = open(destfile, 'w')
		file.write(merger(Cover,Payload,ExtPay))
		file.close()

	elif args[1] == "get":
	
		filetodec = args[2]
		raw = hexstr(filetodec)
		extract = raw.split("6f766572686572656c6f6c7a")
		Ext = extract[1].split("6578746166746572")
		destfile = home +"/Desktop/Embeded" + binascii.unhexlify(Ext[0])
		
		Message = binascii.unhexlify(Ext[1])
		
		file = open(destfile, 'w')
		file.write(Message)
		file.close()
else:
	if len(args) < 3:
		usage(" Error: not enough arguments.",1)
	else:
		usage(" Error: too many arguments.",1)

	

	
