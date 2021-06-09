#! /usr/bin/python3
import socket 
import struct
import textwrap

# Unpack Ethernet Frame 
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H',data[:14])
    return get_mac_addr(dest_mac) , get_mac_addr(src_mac) , socket.htons(proto),data[14:]
    

# Get the MAC Address from the data
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format,bytes_addr)
    mac_address = ':'.join(bytes_str).upper()
    return mac_address


# Unpack IPv4 Packet
def unpack_ipv4_from_data(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl,proto,src_ip,des_ip = struct.unpack('! 8x B B 2x 4s 4s',data[:20])
    # ttl,proto,src_ip,des_ip = struct.unpack('! B B 4s 4s',data[:20])
    return version,header_length,ttl,proto,ipv4(src_ip),ipv4(des_ip),data[header_length:]

def ipv4(addr):
    return '.'.join(map(str,addr))


def unpack_ICMP_packet(data):
    icmp_tyoe ,code,checksum = struct.unpack('!BBH',data[:4])
    return  icmp_tyoe ,code,checksum , data[4:]

def tcp_segment(data):
    src_port,dest_port,sequence,acknowlegdement,offset_reserved_flags = struct.unpack('!HHLLH',data[:14])
    offset = (offset_reserved_flags >> 12)*4
    flags_urg =(offset_reserved_flags & 32) >> 5
    flags_ack = (offset_reserved_flags & 16) >> 5
    flags_psh = (offset_reserved_flags & 8) >> 5
    flags_rst = (offset_reserved_flags & 4) >> 5
    flags_syn = (offset_reserved_flags & 2) >> 5
    flags_fin = offset_reserved_flags & 1
    return src_port,dest_port,sequence,acknowlegdement ,flags_urg,flags_ack,flags_psh,flags_rst,flags_syn,flags_fin,data[offset:]


def udp_segment(data):
    src_port,des_port,size = struct.unpack('!HH 2x H',data[:8])
    return src_port,des_port,size, data[8:]

def format_multiline_data(prefix,string,size=80):
    size -= len(prefix)
    if isinstance(string,bytes):
        string = ''.join(r'\x{:02x}'.format(byte) for byte in string)
        if size%2:
            size-=1
    return '\n'.join([prefix+line for line in textwrap.wrap(string,size)])


if __name__ == "__main__":
    TAB_0 = '[*]'
    TAB_1 = '\t [+]'
    DATA_TAB_1 = '\t  '
    DATA_TAB_2 = '\t\t  '

    s = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))
    while True:
        raw_data , addr = s.recvfrom(65565)
        dest_mac,src_mac,eth_proto,data1 = ethernet_frame(raw_data)
        print("Ethernet/ wlan0 Packet:")
        print(TAB_0+f'Source MAC Address: {src_mac} ==>>  Destination MAC Address: {dest_mac} with Protocol: {eth_proto}')

        # IPv4 Header
        version,header_length,ttl,proto2,src_ip,des_ip,data2 = unpack_ipv4_from_data(raw_data)
        print(TAB_0+"IPv4 Packet: ")
        print(TAB_1+f"Version no.: {version}, Header Length: {header_length}, TTL Value: {ttl}")
        print(TAB_1+f'Source IP Address: {src_ip} ==>>  Destination IP Address: {des_ip}, Protocol: {proto2}')

        # For ICMP packet
        icmp_type ,icmp_code,checksum,data3 = unpack_ICMP_packet(raw_data)
        print(TAB_0+"ICMP Packet:")
        print(TAB_1+f'ICMP Info: ICMP Type: {icmp_type}, ICMP Code: {icmp_code}, Checksum: {checksum}')
        print(TAB_1+f"Data:")
        # print(format_multiline_data(DATA_TAB_2,data3))
            
        # For TCP packet
        src_port1,dest_port1,sequence,acknowlegdement ,flags_urg,flags_ack,flags_psh,flags_rst,flags_syn,flags_fin,data4 = tcp_segment(raw_data)
        print(TAB_0+"TCP Segment: ")
        print(TAB_1+f"Source Port: {src_port1}, Destination Port: {dest_port1}, Sequence number: {sequence}, Acknowlegdement number: {acknowlegdement}")
        print(TAB_1+f"URG Flag: {flags_urg}, ACK Flag: {flags_ack},PSH Flags: {flags_psh}, RST Flags: {flags_rst}, SYN Flag: {flags_syn},FIN Flag: {flags_fin}")
        # print(format_multiline_data(DATA_TAB_2,data4))

        # For UDP Packet
        src_port2,des_port2,size, data5 = udp_segment(raw_data)
        print(TAB_0+"UPD Segment: ")
        print(TAB_1+f"UPD Info: Source Port: {src_port2}, Destinattion Port: {des_port2}, Size: {size}")
        # print(format_multiline_data(DATA_TAB_2,data5))
        print("\n")
