#!/usr/bin/python3
import mechanize
from http.cookiejar import LWPCookieJar

def viewPage(url):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    page = browser.open(url)
    source_code = page.read()
    print(source_code)

def testProxy(url,proxy):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print(source_code)

def testUserAgent(url,userAgent):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders(userAgent)
    page = browser.open(url)
    source_code = page.read()

def cookie_print(url):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    cookie_jar = LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)
    source_code = page.read()
    for cookie in cookie_jar:
        print(cookie)


if __name__ == "__main__":
    url = "https://www.google.com/"
    hideMeProxy = {'http':'216.155.139.115:3128'}
    userAgent = [('User-agent','Mozilla/5.0 (X11; U; '+ 'Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01')]
    # viewPage(url)
    # testProxy(url,hideMeProxy)
    # testUserAgent(url,userAgent)
    # cookie_print(url)