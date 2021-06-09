#!/usr/bin/python3
import requests
from time import sleep
import sys
from bs4 import BeautifulSoup
from threading import Thread,ThreadError
from PIL import Image 
from PIL.ExifTags import TAGS

def find_image(url):
    print("[*] Finding Images in: {}".format(url))
    urlContent = requests.get(url).content
    soup = BeautifulSoup(urlContent,'html.parser')
    imgTags = soup.findAll('img')
    return imgTags
    
def get_image_info(img):
    try:
        exifData = {}
        imgFile = Image.open(img)
        info = imgFile._getexif()
        if info:
            print("\n[+] Information Found related to : {}".format(img))
            for (tag,value) in info.items():
                decoded = TAGS.get(tag,tag)
                exifData[decoded] = value
                print("{}: {}".format(decoded,exifData[decoded]))
            
            exifGPS = exifData['GPSInfo']
            if exifGPS :
                print("[+] {} contains GPS Meta Data".format(img))
            print("\n\n")
        else:
            print("[-] {} does not conatin any Info. <ExifData> ".format(img))

    except:
        print("[-] The {} does not contain any Meta data".format(img)

def downloadImage(img_source,fileName):
    try:
        print("[+] Downloading Image: {}".format(fileName))
        imgContent = requests.get(img_source).content
        with open(fileName,"wb") as imgFile:
            imgFile.write(imgContent)
        return fileName
    
    except Exception as e:
        print("[-] Error: {}".format(e))
        sys.exit()



if __name__ == "__main__":
    usage = 'Usage: python3 img_forensics.py Target_URL <https://example.com>'
    about = "\t1. This Tool Takes an URL \n\t2. Finds Images in given URL \n\t3. Download Images \n\t4. Print Meta Data of Downloaded Images \n"
    if len(sys.argv)!= 2:
        print(usage)
        print("\n"+about)
        sys.exit()

    print("#"*150)
    print(">"*30+"\t\tPython Image Metadata Extractor\t\t"+"<"*30)
    print("#"*150+"\n")
    print("*"*100)
    print("#"*100 + "\n" + about + "#"*100 )
    print("*"*100+"\n")
    url = str(sys.argv[1])
    photos = []
    imgTags = find_image(url)
    for imgtag in imgTags:
        imgName = str(imgtag['src']).split('/')[(len(str(imgtag['src']).split("/")))-1]
        photos.append(imgName)
        img_source = url+imgtag['src']
        threader = Thread(target=downloadImage,args=(img_source,imgName))
        threader.start()
        threader.join()
        if ThreadError:
            sleep(0.05)

    for photo in photos:
        get_image_info(photo)