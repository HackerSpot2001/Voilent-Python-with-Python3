#! /usr/bin/python3
import socket 

# Get Hostname of Your Machine
host = socket.gethostname()

# Get IPv4 using Hostname
socket.gethostbyname(host)
print(socket.getaddrinfo(host,80))

# Get Hostname using an IPv4
socket.gethostbyaddr("103.50.160.20")

# Create a new socket 
# # TCP Protocols
# socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
# socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)
# # UDP Protocols
# socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
# socket.socket(socket.AF_UNIX,socket.SOCK_DGRAM)

# # Create a connection
# socket.create_connection(("192.168.0.120",21))


