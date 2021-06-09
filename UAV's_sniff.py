#!/usr/bin/python3
from scapy.all import *
NAVPORT = 5556
def printPkt(pkt):
    if pkt.haslayer(UDP) and pkt.getlayer(UDP).dport == NAVPORT:
        raw = pkt.sprintf('%Raw.load%')
        print (raw)

conf.iface = 'wlan1mon'
sniff(prn=printPkt)