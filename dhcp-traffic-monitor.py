import os
import sys
import subprocess
from decouple import config

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')
SUDOPASS = config('sudoPass')

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

#use - sudo arp-scan -l -r 3 | grep 192.168.0.11(The IP network of the device)
command = 'sudo arp-scan -l -r 3 | grep 192.168.0.11'
proc = subprocess.Popen(['sudo','arp-scan', '-l', '-r 3','grep', IP_NETWORK], stdout=subprocess.PIPE)




while True:
    line = proc.stdout.readline()
    print(line)
    
    if not line:
        break

        