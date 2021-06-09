#!/usr/bin/python3
import geocoder
from socket import gethostbyname

""" Getting Location and More information using IP Address"""
def get_info_about_ip(target):
    try:
        ip = gethostbyname(target)
        info = geocoder.ipinfo(ip)
        for data in info.json:
            print("{}:- {}".format(data,info.json[data]))

    except Exception as e:
        print(e)

        
if __name__ == "__main__":
    print("Get Info about IP or Host")
    target = str(input("Enter Target <IP or Hostname>:- "))
    get_info_about_ip(target)

"""     Getting Location Using pygeoip  
import pygeoip
def print_record(target):
    g1 = pygeoip.GeoIP("geo.dat")
    rec = g1.record_by_name(target)
    city = rec['city']
    # region = rec['region_name']
    country = rec['country_name']
    long = rec['longitude']
    lat = rec['latitude']
    print("Target {} Geo-located".format(target))
    print("City: "+str(city))
    # print("Region: "+str(region))
    print("Country: "+str(country))
    print("Longitute: "+str(long))
    print("Latitute: "+str(lat))



if __name__ == "__main__":
    print_record("103.58.41.175")

"""