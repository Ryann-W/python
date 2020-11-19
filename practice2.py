# --------------------  extract XML  ------------------

mport urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

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

# --------------------  extract XML  ------------------



