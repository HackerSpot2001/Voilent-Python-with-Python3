#!/usr/bin/python3
import socket
import struct

s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_TCP)
while True:
    packet = s.recvfrom(65565)
    packet = packet[1]
    ip_header = packet[0:20]
    print(ip_header[0])