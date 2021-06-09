#! /usr/bin/python3
import socket
import sys
from threading import Thread, ThreadError
from time import sleep

def PortScanner(ip,port):
    socket.setdefaulttimeout(1)
    try:
        new_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        new_socket.connect((ip,port))
        result = new_socket.recv(1024)
        print("[+]Port {}/tcp is open".format(port))
        print("[*] {}\n\n".format(result))
        new_socket.close()
    except:
        pass
        
# def PortScanner(ip,port):
#     socket.setdefaulttimeout(0.5)
#     new_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     result= new_socket.connect_ex((ip,port))
#     # print("[-] Testing Port {}".format(port))
#     if not result:
#         print("[+]Port {}/tcp is open".format(port))
    

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("*"*60)
        print("*"*60)
        print("####\t\tpython3 portScanner.py target\t\t####")
        print("*"*60)
        print("*"*60)
        sys.exit()

    # print("*"*60)
    print("#"*60)
    print("****\t\tPython3 Port Scanner\t\t\t****")
    print("#"*60)
    
    try:
        target = socket.gethostbyname(str(sys.argv[1]))
    except:
        print("[-]Host [{}] not resolve".format(sys.argv[1]))
        sys.exit()
    
    ports = 65535
    print("[+] Scanning {}[{}] all Ports {}".format(sys.argv[1],target,ports))
    for port in range(ports):
        threader = Thread(target=PortScanner,args=(target,port))
        threader.start()
        if ThreadError:
            sleep(0.003)