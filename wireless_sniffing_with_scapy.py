#!/usr/bin/python3
from scapy.all import *
def printPacket(packet):
    if packet.haslayer(Dot11Beacon):
        print("[+] Detected 802.11 Beacon Frame")
    
    elif packet.haslayer(Dot11ProbeReq):
        print("[+] Detected 802.11 Probe Request Frame")
    
    elif packet.haslayer(TCP):
        print("[+] Detected TCP Packet")
    
    elif packet.haslayer(DNS):
        print("[+] Detected DNS Packet")


if __name__ == "__main__":
    conf.iface = 'wlan1mon'
    # sniff(prn=printPacket)