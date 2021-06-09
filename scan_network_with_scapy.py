#!/usr/bin/python3

import scapy.all as newScapy

# request = newScapy.ARP()
# request.pdst = '192.168.0.1/24'
# broadcast = newScapy.Ether() 
  
# broadcast.dst = 'ff:ff:ff:ff:ff:ff'
  
# request_broadcast = broadcast / request 
# clients = newScapy.srp(request_broadcast,timeout=5)[0] 
# for element in clients: 
#     print(element[1].psrc + "      " + element[1].hwsrc)

target_ip = '192.168.1.1/24'
arp = newScapy.ARP(pdst= target_ip)
ether = newScapy.Ether(dst='ff:ff:ff:ff:ff:ff')
packet = ether/arp
result = newScapy.srp(packet,timeout=3)[0]
clients = []

for (sent,recieve) in result:
    clients.append({'ip':recieve.psrc,'mac':recieve.hwsrc})

print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))