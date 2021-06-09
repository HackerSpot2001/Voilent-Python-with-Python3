#!/usr/bin/python3
from scapy.all import *

def sniffProbe(p):
    if p.haslayer(Dot11):
        wifiMac = p.getlayer(Dot11).addr2
        print(wifiMac)















# def sniffProbe(p):
#     if p.haslayer(Dot11ProbeReq):
#         netName = p.getlayer(Dot11ProbeReq).info
#         netName = netName.decode()
#         if netName not in probeRequest:
#             if netName != '':
#                 probeRequest.append(netName)
#                 print( '[+] Detected New Probe Request: '+netName)
#             else:
#                 pass

#         else:
#             pass

if __name__ == "__main__":
    probeRequest = []
    sniff(iface="wlan1mon",prn=sniffProbe)