import os
import sys
import subprocess
from decouple import config
from time import  sleep
#import app

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')


proc = subprocess.Popen(['ping', IP_NETWORK], stdout=subprocess.PIPE)

while True:
    
    line = proc.stdout.readline()

    if not line:
        flag = 1
        break
        
    connected_ip = line.decode('utf-8').split()[3]
    print(connected_ip)
    sleep(2)
    
    new_IP = IP_NETWORK + ":"
    print(new_IP)

    if connected_ip == new_IP:
        flag = 0
        break
        

if(flag == 0):
    print("Arnab\'s home")
    
    subprocess.call(["python3", "app.py"])
    #app.spotifyBot()

else:
    print('Arnab\'s not home')

#To sniff the DHCP traffic for the device to reconnect


"""

#use - sudo arp-scan -l -r 3 | grep 192.168.0.11(The IP network of the device) 'grep', IP_NETWORK
command = 'sudo arp-scan -l -r 3 | grep 192.168.0.11'


proc = subprocess.Popen(['sudo','arp-scan', '-l', '-r 3',], stdout=subprocess.PIPE)




while True:

    line = proc.stdout.readline()
    ip_save = []

    for ch in line:
        
        if(ch == '\t'):
            break
        else:
            ip_save.append(str(ch))

    
    #print(ip_save)

    print(line)
    
    
    connected_ip = line.decode('utf-8').split()[0]
    
    
    if not line:
        break

        """