#!/usr/bin/python3
import ftplib

"""
def returnDefault(ftp):
    try:
        print("We Founded On {}".format(ftp.host))
        print(ftp.nlst())
    except Exception as e:
        print(e)



"""
def returnDefault(ftp):
    try:
        dirList = ftp.nlst()
        # print(dirList)
    except:
        dirList = []
        print("[-] Could not list Directory Content")
        print("[-] Skipping to next Content")
    
    retList = []
    for fileName in dirList:
        fn = fileName.lower()
        if ".php" in fn or ".htm" in fn or ".asp" in fn:
            print("[+] Found Page {}".format(fileName))
            retList.append(fileName)
    return retList

if __name__ == "__main__":
    host = "192.168.0.106"
    username = "msfadmin"
    password = "msfadmin"
    ftp = ftplib.FTP(host,username,password)
    # ftp.login(username,password)
    returnDefault(ftp)