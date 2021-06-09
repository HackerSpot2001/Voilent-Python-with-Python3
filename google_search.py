#!/usr/bin/python3
import googlesearch
import urllib
from mechanize import Browser
import json

class Google_Result:
    def __init__(self,title,text,url):
        self.title = title
        self.text = text
        self.url = url
    
    def __repr__(self):
        return self.title
    
def google(search_item):
    browser = Browser()
    browser.set_handle_robots(False)
    search_item = urllib.parse.quote_plus(search_item)
    response = browser.open('http://ajax.googleapis.com/'+'ajax/services/search/web?v=1.0&q='+ search_item)
    obj = json.load(response)
    results = []
    for result in obj['responseData']['results']:
        url = result['url']
        title = result['title']
        text = result['text']
        new_gr = Google_Result(title,text,url)
        results.append(new_gr)
        return results

def google_search(search_item):
    num = 1
    for j in googlesearch.search(search_item,tld="co.in", num=10, stop=15, pause=2):
        print("{}. {}".format(num,j))
        num+=1


if __name__ == "__main__":
    google_search("New Delhi")