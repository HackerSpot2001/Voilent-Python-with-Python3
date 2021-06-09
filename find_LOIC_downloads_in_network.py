import dpkt
import socket

def findDownloads(pcap):
    for (ts,buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            tcp = ip.data
            http = dpkt.http.Request(tcp.data)
            if http.method == "GET":
                url = http.uri.lower()
                if '.zip' in url and 'loic' in url:
                    print('[!] '+src+' Downloaded LOIC')
        except:
            pass

f = open('test.pcap',"rb")
pcp = dpkt.pcap.Reader(f)
findDownloads(pcp)