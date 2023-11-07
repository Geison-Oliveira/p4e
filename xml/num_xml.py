# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml
# Actual data: http://py4e-data.dr-chuck.net/comments_1772110.xml

import urllib.request, urllib.parse, urllib.request
import ssl
import xml.etree.ElementTree as ET

url = input('Enter location: ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', url)
x_file = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(x_file), 'characters')
tree = ET.fromstring(x_file)
counts = tree.findall('comments/comment/count')
add = 0
tot = 0
for count in counts:
    add = add + int(count.text)
    tot = tot + 1
print('Count:', tot)
print('Sum:', add)