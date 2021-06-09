#!/usr/bin/python3
from subprocess import check_output
ifconfig = check_output(['ifconfig','wlan0'])
iface,ip,mac, Bcast, Nmask,IPv6 = (ifconfig.split()[i] for i in (0,5,17,9,7,11))
print("Iface:- {}".format(iface))
print("IPv4:- {}".format(ip))
print("IPv6:- {}".format(IPv6))
print("MAC Address:- {}".format(mac))
print("Braodcast Name: {}".format(Bcast))
print("Nmask: {}".format(Nmask))