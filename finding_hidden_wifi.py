#!/usr/bin/python3
from scapy.all import *

def find_hidden_wifi(pkt):
    if pkt.haslayer(Dot11Beacon):
        print(pkt.getlayer(Dot11Beacon).info)
        if pkt.getlayer(Dot11Beacon).info == '':
            addr2 = pkt.getlayer(Dot11).addr2
            if addr2 not in hiddenNets:
                hiddenNets.append(addr2)
                print("[+] Detected Hidden SSID with MAC: {}".format(addr2))


if __name__ == "__main__":
    hiddenNets = []
    sniff(iface = 'wlan1mon',prn=find_hidden_wifi)