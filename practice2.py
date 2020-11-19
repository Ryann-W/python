# --------------------  extract XML  ------------------

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
'''
url = 'http://py4e-data.dr-chuck.net/comments_1071074.xml'

uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()

print(data.decode())

tree = ET.fromstring(data)

counts = tree.findall('.//count')

total = 0

for count in counts:
    total = total + int(count.text)
print(total)
'''
# --------------------  extract XML  ------------------


url_json = 'http://py4e-data.dr-chuck.net/comments_1071075.json'

uh_json = urllib.request.urlopen(url_json,context = ctx)


data_json = json.loads(uh_json.read())

# print(data_json)

extract_data = data_json.get('comments',None)

# print(extract_data)

total = 0

for item in extract_data:
    total = total + int(item.get('count',None))

print(total)