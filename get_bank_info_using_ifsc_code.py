#!/usr/bin/python3
import requests


def get_info(ifsc_code):
    url = 'https://ifsc.razorpay.com/'
    try:
        result = requests.get(url+ifsc_code).json()
        print("Centre: {}".format(result['CENTRE'])) 
        print("Contact: {}".format(result['CONTACT']))
        print("UPI: {}".format(result['UPI']))
        print("CITY: {}".format(result['CITY']))
        print("STATE: {}".format(result['STATE']))
        print("DISTRICT: {}".format(result['DISTRICT']))
        print("IMPS: {}".format(result['IMPS']))
        print("ADDRESS: {}".format(result['ADDRESS']))
        print("BRANCH: {}".format(result['BRANCH']))
        print("BANK: {}".format(result['BANK']))
        print("BANKCODE: {}".format(result['BANKCODE']))
        print("IFSC: {}".format(result['IFSC']))
        print("RTGS: {}".format(result['RTGS']))
        print("NEFT: {}".format(result['NEFT']))
        print("MICR CODE: {}".format(result['MICR']))
        print("STD CODE: {}".format(result['STD']))
    except:
        pass

if __name__ == "__main__":
    IFSC = 'SBIN0004741'
    get_info(IFSC)