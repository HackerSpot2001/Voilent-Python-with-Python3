#!/usr/bin/python3
import PyOBEX
try:
    btPrinter =PyOBEX.client(PyOBEX.BLUETOOTH)
    btPrinter.connect('00:16:38:DE:AD:11', 2)
    btPrinter.put_file('/tmp/ninja.jpg')
    print ('[+] Printed Ninja Image.')
except:
    print ('[-] Failed to print Ninja Image.')