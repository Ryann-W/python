# --------------------  extract XML  ------------------
'''
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

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

'''
#--------------------- extract JSON ------------------

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

#--------------------- extract JSON ------------------

'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)