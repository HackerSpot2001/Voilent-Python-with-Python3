import socket 
import dpkt

thresh = 10000
def find_Attack(pcap):
    pktCount = []
    for (ts,buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            dport = tcp.dport
            if dport == 80:
                stream = src + ':' + dst
            if pktCount.haskey(stream):
                pktCount[stream] = pktCount[stream] + 1
            else:
                pktCount[stream] = 1
        except:
            pass

    for stream in pktCount:
        pktsSent = pktCount[stream]
        if pktsSent > thresh:
            src = stream.split(':')[0]
            dst = stream.split(':')[1]
            print ('[+] '+src+' attacked '+dst+' with ' \
            + str(pktsSent) + ' pkts.')

pcp = dpkt.pcap.Reader(open("test.pcap","rb"))
find_Attack(pcp)