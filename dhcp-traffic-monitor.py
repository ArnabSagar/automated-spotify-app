import os
import sys
import subprocess
from decouple import config

#os.environ['IP_NETWORK'] = '192.168.0.11'
# os.environ['IP_DEVICE'] = '192.168.0.11'

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')

proc = subprocess.Popen(['ping', IP_NETWORK], stdout=subprocess.PIPE)

while True:
    line = proc.stdout.readline()
    print(line)
    
    if not line:
        break
        
    connected_ip = line.decode('utf-8').split()[3]

    if connected_ip == IP_DEVICE:
        subprocess.Popen(['say', 'Arnab\'s phone just connected'])

#To sniff the DHCP traffic for the device to reconnect