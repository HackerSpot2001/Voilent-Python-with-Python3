#!/usr/bin/python3
from scapy.all import *
import sys

def sniffDot11(pkt):
    if pkt.haslayer(Dot11ProbeResp):
        addr2 = pkt.getlayer(Dot11).addr2
        if (addr2 in hiddenNets) & (addr2 not in unhiddenNets):
            netName = p.getlayer(Dot11ProbeResp).info
            print("[+] Detected Hidden SSID: {}, for MAC: {} ".format(netName,addr2))
            unhiddenNets.append(addr2)
    
    if pkt.haslayer(Dot11Beacon):
        if pkt.getlayer(Dot11Beacon).info == '':
            addr2 = pkt.getlayer(Dot11).addr2
            if addr2 not in hiddenNets:
                print("[-] Detected hidden SSID: for MAC: {}".format(addr2))
                hiddenNets.append(addr2)


if __name__ == "__main__":
    hiddenNets = []
    unhiddenNets = []
    sniff(iface='wlan1mon',prn=sniffDot11)