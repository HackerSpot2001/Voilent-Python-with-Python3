#!/usr/bin/python3
import requests
import html5lib
from bs4 import BeautifulSoup

url = "https://codewithharry.com"
# url = "https://www.google.com"
raw_content = requests.get(url)

# For an HTML Content
htmlContent = raw_content.content
# print(htmlContent)

# For an HTML Content
# linksContent = raw_content.links
# print(linksContent)

soup = BeautifulSoup(htmlContent,'html.parser')

# Get the title of the HTML page
title = soup.title
head = soup.head
# print(soup)
# print(soup.prettify)

# # Objects in Beautiful Soup
# print(type(soup)) # 1. BeautifulSoup
# print(type(title)) # 2. Tag
# print(type(title.string)) # 3. NavigableString
# # 4. Comment

# Get all Paragraphs using soup
# paras = soup.find_all('p')
# print(paras)

# Get all Anchor tags using soup
# anchorTag = soup.find_all('a')
# print(anchor)

# Get the first element of any Tag of HTML Page
# print(soup.find('p'))
# Get the Classes of first element of any Tag of HTML Page
# print(soup.find('p')['class'])

# Find all Tags and elements which is linked with class lead
# print(soup.find_all('p',class_="lead"))

# Get the text from the elements
# print(soup.find('p').get_text())

# get all links from an anchor tags 
anchorTag = soup.find_all('a')
all_link = set()
for link in anchorTag:
    if (link.get('href') != '#'):
        linkText = f"{url}{link.get('href')}"
        all_link.add(linkText)
    
for links in all_link:
    print(links)