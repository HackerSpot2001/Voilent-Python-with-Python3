#!/usr/bin/python3
import mechanize
from http import cookiejar
import random
from time import sleep

class AnonBrowser(mechanize.Browser):
    def __init__(self,proxy=[],userAgent=[]):
        mechanize.Browser.__init__(self)
        self.set_handle_robots(False)
        # self.set_proxies(proxy)
        # self.addheaders(userAgent + ['Mozilla/4.0 ', 'FireFox/6.01','ExactSearch', 'Nokia7110/1.0'])
        self.set_cookiejar(cookiejar.LWPCookieJar())
        # self.anonymize()

    def clear_cookie(self):
        self.set_cookiejar(cookiejar.LWPCookieJar())
    
    def change_user_agent(self):
        index = random.randrange(0,len(self.userAgent))
        
    def change_proxy(self):
        if self.proxies:
            index = random.randrange(0, len(self.proxies))
            self.set_proxies({'http': self.proxies[index]})

    def anonymize(self, sleep = False):
        self.clear_cookies()
        self.change_user_agent()
        self.change_proxy()
        if sleep:
            sleep(60)



if __name__ == "__main__":
    url = "https://www.google.com"
    browser = AnonBrowser()
    browser.open(url)