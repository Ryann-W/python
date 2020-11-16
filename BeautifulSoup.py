
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

url = input('Enter - ')


html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrive all of the anchor tags

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

# Python for Web Service
# Data on the web
# agreed way to represent data going between application and across networks
# two commonly used formats: XML and JSON
