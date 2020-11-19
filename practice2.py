import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

# print(data.decode())

tree = ET.fromstring(data)

results = tree.findall('comments')
print(results)
#name = results[0].find('name').text
#count = results[0].find('count').text
#name = tree.find('name').text
#count = tree.find('count').text
#print(results)

#print("this is the name",name)
#print("this is the count",count)


# name = results[0].find('comment').find('name').text
# print(name)

