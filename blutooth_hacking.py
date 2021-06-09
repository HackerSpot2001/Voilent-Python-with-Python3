#!/usr/bin/python3
from bluetooth import *

# devList = discover_devices()
# for device in devList:
#     name = str(lookup_name(device))
#     print("[+] Device Name: {}".format(str(name)))
#     print("[+] MAC Address: {}\n".format(str(device)))

def findDevices():
    foundDevs = discover_devices(lookup_names=True)
    for (addr,name) in foundDevs:
        if addr not in alreadyFOund:
            alreadyFOund.append(str(addr))
            print("[+] Device Found: {}".format(str(name)))
            print("[+] MAC Address: {}".format(str(addr)))

def retBtAddr(addr):
    btAddr=str(hex(int(addr.replace(':', ''), 16) + 1))[2:]
    btAddr=btAddr[0:2]+":"+btAddr[2:4]+":"+btAddr[4:6]+":"+btAddr[6:8]+":"+btAddr[8:10]+":"+btAddr[10:12]
    return btAddr

def checkBluetooth(btAddr):
    btName = lookup_name(btAddr)
    if btName:
        print ('[+] Detected Bluetooth Device: ' + btName)
    else:
        print ('[-] Failed to Detect Bluetooth Device.')

def wifiPrint(pkt):
    Device  = 'd0:23:db'
    if pkt.haslayer(Dot11):
        wifiMAC = pkt.getlayer(Dot11).addr2
        if Device == wifiMAC[:8]:
            print( '[*] Detected iPhone MAC: ' + wifiMAC)
            btAddr = retBtAddr(wifiMAC)
            print ('[+] Testing Bluetooth MAC: ' + btAddr)
            checkBluetooth(btAddr)


def rfcommCon(addr, port):
    sock = BluetoothSocket(RFCOMM)
    try:
        sock.connect((addr, port))
        print ('[+] RFCOMM Port ' + str(port) + ' open')
        sock.close()
    except Exception, e:
        print ('[-] RFCOMM Port ' + str(port) + ' closed')

def BT_service_discovery_protocal(addr):
    services = find_service(address=addr)
    for service in services:
        name = service['name']
        proto = service['protocol']
        port = str(service['port'])
        print('[+] Found ' + str(name)+' on '+ str(proto) + ':'+port)



if __name__ == "__main__":
    alreadyFOund= []
    while  True:
        findDevices()
        print(alreadyFOund)
    for port in range(1, 30):
        rfcommCon('00:16:38:DE:AD:11', port)

    BT_service_discovery_protocal('00:16:38:DE:AD:11')