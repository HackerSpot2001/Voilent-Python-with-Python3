#!/usr/bin/python3
import os 
import socket

user = os.getlogin()
host = socket.gethostname()
cwd = os.getcwd()
while True:
    inp = input("{}@{}$[{}]: ".format(user,host,cwd))
    os.system(inp)
os.system("bash")