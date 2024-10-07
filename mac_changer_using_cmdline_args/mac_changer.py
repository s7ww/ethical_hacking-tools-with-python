#!/usr/bin/env python3

import subprocess
import optparse  # to create command line arguement

parser = optparse.OptionParser() #object to hanlde user cmd line input

parser.add_option("-i","--interface",dest="interface",help="interface to change mac address")
parser.add_option("-m","--mac",dest="new_mac",help=" new mac address")
#using the method provided by the object

(options, arguments)= parser.parse_args() #seperates the user input and assigns to respective variales


# Get interface and new MAC address from user
interfacez = options.interface
new_mac = options.new_mac

# Change the MAC address
subprocess.call(f"sudo ifconfig {interfacez} down", shell=True)
subprocess.call(f"sudo ifconfig {interfacez} hw ether {new_mac}", shell=True)
subprocess.call(f"sudo ifconfig {interfacez} up", shell=True)

# Display the current network configuration
subprocess.call("ip addr show", shell=True)
