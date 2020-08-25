import subprocess
from decouple import config
from time import  sleep

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')

#To sniff the DHCP traffic for the device to reconnect
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
    
else:
    print('Arnab\'s not home')