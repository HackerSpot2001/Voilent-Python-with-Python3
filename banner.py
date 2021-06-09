#! /usr/bin/python3
import socket
import sys
import os

"""
def retBanner(ip,port):
    socket.setdefaulttimeout(3)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s = socket.socket()
    try:
        s.connect((ip,port))
        ans = str(s.recv(1024))
        s.close()
        return ans

    except Exception as e:
        print("Error == {}".format(str(e)))
    
def checkVuln(banner):
    if 'vsFTPd' or "2." in banner:
        print("FTP Version is Vulnrable")
    elif 'FreeFloat Ftp Server (Version 1.00)' in banner :
        print("FreeFloat FTP Version is Vulnrable")
    elif 'Ability Server 2.34' in banner:
        print("Ability Server FTP Version is Vulnrable")
    elif 'Sami FTP Server 2.0.2' in banner: 
        print("Sami FTP Version is Vulnrable")
    else:
        print("FTP Version is not Vulnrable")

if __name__ == "__main__":
    usage = "python3 banner.py TARGET_IP PORT"
    if len(sys.argv) !=3: 
        print(usage)
        sys.exit()
    
    try: 
        target = socket.gethostbyname(sys.argv[1])

    except socket.gaierror:
        print("Target not Resolve!")
        sys.exit()
    
    port = int(sys.argv[2])
    banner = retBanner(target,port)
    checkVuln(banner)
"""


"""
def retBanner(ip,port,filename):
    try:
        target = socket.gethostbyname(ip)
    except socket.gaierror:
        print("Host Not resolve")
        sys.exit()

    socket.setdefaulttimeout(3)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((target,port))
    ans = str(s.recv(1024))
    with open("{}".format(filename), "a") as f:
        if 'vsFTPd' or "2." in ans:
            f.write("{}:{} FTP Version Vulnrable\n".format(target,port))

if __name__ == "__main__":
    usage = "python3 test.py target port filename"
    if (len(sys.argv) !=4):
        print(usage)
        sys.exit()
    
    ip = sys.argv[1]
    port = int(sys.argv[2])
    filename = sys.argv[3]
    retBanner(ip,port,filename)
    
"""