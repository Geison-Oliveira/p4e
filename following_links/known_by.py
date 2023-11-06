# Sample problem: http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Actual problem: http://py4e-data.dr-chuck.net/known_by_Wendy.html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position) - 1
def tag_soup(link):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags
print('Retrieving:', url)
while count > 0:
    a_tags = tag_soup(url)
    url = a_tags[position]
    url = url.get('href', None)
    print('Retrieving:', url)
    count = count - 1