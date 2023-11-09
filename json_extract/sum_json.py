# Sample data: http://py4e-data.dr-chuck.net/comments_42.json
# Actual data: http://py4e-data.dr-chuck.net/comments_1772111.json

import urllib.request, urllib.parse, urllib.error
import json

while True:
    url = input('Enter location: ')
    if len(url) < 1:
        break
    print('Retrieving:', url)
    url_handle = urllib.request.urlopen(url)
    data = url_handle.read().decode()
    print('Retrieved:', len(data), 'characters')
    jsn = json.loads(data)
    summ = 0
    for num in jsn['comments']:
        summ = summ + int(num['count'])
    print(summ)