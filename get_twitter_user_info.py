#!/usr/bin/python3
import urllib
import json
from mechanize import Browser


class reconPerson:
    def __init__(self,first_name,last_name,job='',social_media={}):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.social_media = social_media
    
    def __repr__(self):
        return self.first_name+" "+self.last_name+" has job "+self.job
    
    def get_social_media(self,media_name):
        if self.social_media[media_name]:
            return self.social_media[media_name]
        
        return None
    
    def query_twitter(self,query):
        query = urllib.parse.quote_plus(query)
        results = []
        br = Browser()
        br.set_handle_robots(False)
        responce = br.open('http://twitter.com/search.json?q={}'.format(query))
        responce = responce.read()
        responce = responce.decode()
        json_obj = json.load(responce)
        for result in json_obj['results']:
            new_result = {}
            new_result['from_user'] = result['from_user_name']
            new_result['geo'] = result['geo']
            new_result['tweet'] = result['text']
            results.append(new_result)
        return results

    def twitter_locate(tweets,cities):
        locations = []
        locCnt = 0
        cityCnt = 0
        tweetsText = ""
        for tweet in tweets:
            if tweet['geo'] != None:
                locations.append(tweet['geo'])
                locCnt += 1
                tweetsText += tweet['tweet'].lower()

        for city in cities:
            if city in tweetsText:
                locations.append(city)
                cityCnt+=1

        print ("[+] Found "+str(locCnt)+" locations "+"via Twitter API and "+str(cityCnt)+" locations from text search.")
        return locations

def load_cities(cityFile):
    cities = []
    for line in open(cityFile).readlines():
        city=line.strip('\n').strip('\r').lower()
        cities.append(city)

    return cities

def get_tweets(handle):
    query = urllib.quote_plus('from:' + handle+' since:2009-01-01 include:retweets')
    tweets = []
    browser = anonBrowser()
    browser.anonymize()
    response = browser.open('http://search.twitter.com/'+'search.json?q='+ query)
    json_objects = json.load(response)
    for result in json_objects['results']:
        new_result = {}
        new_result['from_user'] = result['from_user_name']
        new_result['geo'] = result['geo']
        new_result['tweet'] = result['text']
        tweets.append(new_result)
    return tweets


if __name__ == "__main__":
    query = 'from:th3j35t3r since:2010-01-01 include:retweets'
    ab = reconPerson('Boondock', 'Saint')
    print(ab.query_twitter(query))