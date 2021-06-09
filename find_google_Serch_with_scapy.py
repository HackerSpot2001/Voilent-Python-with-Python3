#!/usr/bin/python3
from scapy.all import *
import re

def find_google(pkt):
    print(pkt)
    if pkt.haslayer(Raw):
        payload = pkt.getlayer(Raw).load
        if 'GET' in payload:
            print("Raw: "+payload)
            if 'google' in payload:
                r = re.findall(r'(?i)\&q=(.*)\&',payload)
                if r:
                    search = r[0].split('&')[0]
                    search = search.replace('q=','').replace('+'," ").replace('%20'," ")
                    print("search Query: {}".format(search))


if __name__ == "__main__":
    conf.iface = 'wlan0'
    print ('[*] Starting Google Sniffer.')
    sniff(filter='tcp port 80', prn=find_google)