import os
import sys
import subprocess
from decouple import config

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')

"""
proc = subprocess.Popen(['ping', IP_NETWORK], stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    print(line)
    
    if not line:
        break
        
    connected_ip = line.decode('utf-8').split()[3]

    if connected_ip == IP_DEVICE:
        print("Arnab\'s home")
        subprocess.Popen(['say', 'Arnab\'s phone just connected'])

#To sniff the DHCP traffic for the device to reconnect


"""

proc1 = subprocess.Popen(['sudo','arp-scan', '-l','-r 3'], stdout=subprocess.PIPE)

line = proc1.stdout.readline()
print(line)