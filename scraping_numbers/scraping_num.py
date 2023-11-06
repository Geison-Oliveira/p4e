# Sample data: http://py4e-data.dr-chuck.net/comments_42.html
# Actual data: http://py4e-data.dr-chuck.net/comments_1772108.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
tags = soup('span')
summ = 0
for tag in tags:
    c = tag.contents[0]
    c = int(c)
    summ = summ + c
print(summ)