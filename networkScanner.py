#!/usr/bin/python3
import socket
import threading

def ipPort_Scanner(ip,port):
    ip = str(ip)
    s = socket.socket()
    ans = s.connect_ex((ip,port))
    print("Scanning {}".format(ip))
    if not ans:
        print("IP {} : Port {} is open".format(ip,port))
    s.close()

for x in range(1024):
    for y in range(255):
        ip = '192.168.1.{}'.format(y)
        ipPort_Scanner(ip,x)
        # thre = threading.Thread(target=ipPort_Scanner,args=(ip,x))
        # thre.start()