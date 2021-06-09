#!/usr/bin/python3
from mechanize import *
from bs4 import BeautifulSoup
import os
import re

def get_links(url):
    browser = Browser()
    browser.set_handle_robots(False)
    page = browser.open(url)
    htmlContent = page.read()
    try:
        print("[+] Printing Links:")
        soup = BeautifulSoup(htmlContent,'html.parser')
        links = soup.find_all('a')
        for link in links:
            linktext = link.get('href')
            if (linktext not in all_links) and ('#' not in linktext): 
                print("[+] URL: {}{}".format(url,linktext))
                all_links.add(linktext)

    except:
        pass


def mirrorImage(url,direc):
    try:
        browser = Browser()
        browser.set_handle_robots(False)
        page = browser.open(url)
        htmlContent = page.read()
        soup = BeautifulSoup(htmlContent,'html.parser')
        img_tages = soup.findAll('img')
        for img in img_tages:
            filename = img['src']
            filename = os.path.join(direc,(filename.replace('/','_')))
            print("[+] Saving {}".format(str(filename)))
            try:
                for ext in extensions:
                    if ext in filename:
                        if 'http://' not in img['src'] or 'https://' not in img['src']:
                            url1 = url+img['src']
                            data = browser.open(url1).read()
                            browser.back()
                            save = open(filename,'wb')
                            save.write(data)
                            save.close()
                            
                        else:
                            data = browser.open(img['src']).read()
                            browser.back()
                            save = open(filename,'wb')
                            save.write(data)
                            save.close()

            except Exception as e:
                print("[!] Error: {}".format(str(e)))

    except:
        pass
            

    
if __name__ == "__main__":
    extensions = ['.webp','.jpeg','.png','.gif','.jpg','.tiff','.psd','ai','indd','.raw']
    all_links = set()
    url = "http://www.jbcollege.in/"
    get_links(url)
    mirrorImage(url,"/home/hacker/Downloads/")