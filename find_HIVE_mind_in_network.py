import socket
import dpkt

def find_HIVE(pcap):
    for (ts,buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            tcp = ip.data
            s_port = tcp.sport
            d_port = tcp.dport
            if d_port == 6667:
                if '!lazor' in tcp.data.lower():
                    print('[!] DDoS Hivemind issued by: '+src)
                    print ('[+] Target CMD: ' + tcp.data)
            elif s_port == 6667:
                if '!lazor' in tcp.data.lower():
                    print( '[!] DDoS Hivemind issued to: '+src)
                    print ('[+] Target CMD: ' + tcp.data)
            else:
                print("TS:- {}".format(ts))
                print("Buf:- {}".format(buf))

        except:
            pass
try:
    f = open('test.pcap',mode="rb")
    pcp = dpkt.pcap.Reader(f)
    find_HIVE(pcp)
except Exception as e:
    print("Error Occured:-")
    print(e)