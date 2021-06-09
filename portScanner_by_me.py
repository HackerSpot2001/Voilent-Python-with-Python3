import socket
import sys
import threading

"""

#! /usr/bin/python3
import socket
import sys
import threading
# import time

'''
To write Our PortScanner We will break our script in some steps
1. get Hostname and convert it into an ipv4 or ipv6
2. Write an list of common ports 
3. determine a version of a specific port 
4. send the data and collect the recieved Application data(banner)
'''

def PortScanner(ip,port):
    socket.setdefaulttimeout(1)
    create_conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = create_conn.connect_ex((ip,port))
    if not result:
        print("[*]Port {}/tcp is open".format(port))



if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("*"*60)
        print("#"*60)
        print("*"*60)
        print("####\t\t\t\t\t\t\t####")
        print("****\t\tpython3 portScanner.py target\t\t****")
        print("####\t\t\t\t\t\t\t####")
        print("*"*60)
        print("#"*60)
        print("*"*60)
        sys.exit()

    print("*"*60)
    print("#"*60)
    print("*"*60)
    print("####\t\t\t\t\t\t\t####")
    print("****\t\tPython Port Scanner\t\t\t****")
    print("####\t\t\t\t\t\t\t####")
    print("*"*60)
    print("#"*60)
    print("*"*60)
    
    try:
        target = socket.gethostbyname(str(sys.argv[1]))
    except:
        print("[-]Host [{}] not resolve".format(sys.argv[1]))
        sys.exit()
    
    print("Scanning {}[{}]".format(sys.argv[1],target))
    for port in range(65536):
        threader = threading.Thread(target=PortScanner,args=(target,port))
        threader.start()



"""
"""
use = "python3 portScanner_by_me.py TARGET START_PORT END_PORT"
print("#"*100)
print("\tPython Port Scanner\t")
print("#"*100)
if (len(sys.argv) != 4):
    print(use)
    sys.exit()

try: 
    target = socket.gethostbyname(sys.argv[1])

except socket.gaierror :
    print("Target not Resolve!")
    sys.exit()

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

def portScanningPhase(ip,port):
    # print("Scanning ports {}".format(port))
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    res = s.connect_ex((ip,port))
    if (not res):
        print("Port {} is Open".format(port))
    s.close()


for port in range(start_port,end_port+1):
    thread = threading.Thread(target=portScanningPhase,args=(target,port))
    thread.start()

"""