#!/usr/bin/env python

import subprocess
import optparse
import re



def getArgs():
	parser = optparse.OptionParser() #python mac_changer.py --help

	parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
	parser.add_option("-m", "--mac", dest="newMac", help="Interface to change its MAC address")

	(options, args) = parser.parse_args()
	if not options.interface:
		# code to handle error
		parser.error("[-] Please specify an interface")
	elif not options.newMac:
		# code to handle error
		parser.error("[-] Please specifuy an mac")
				
	return options

def changeMac(interface, newMac):
	print("[+] Changing MAC address for "+interface+" to "+newMac)

	subprocess.call(["ifconfig ", interface, "down"])
	subprocess.call(["ifconfig ", interface, " hw ether ", newMac])
	subprocess.call("ifconfig "+interface+" up")

def getCurrentMac():
	ifconfig = subprocess.check_output(["ifconfig"])
	ifconfig = ifconfig.decode('utf-8')
	
	res = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig)

	if res:
		return res.group(0)
	else:
		print("[-] Could not read MAC address.")

	return None

		
print(getCurrentMac());
#options = getArgs()

#changeMac(options.interface, options.newMac)

