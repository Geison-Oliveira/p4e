import urllib.request, urllib.parse, urllib.error
import ssl
import json

service_url = 'http://py4e-data.dr-chuck.net/json?'
while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break
    arg = dict()
    arg['address'] = address
    arg['key'] = 42

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = service_url + urllib.parse.urlencode(arg)
    print('Retrieving:', url)
    url_handle = urllib.request.urlopen(url, context=ctx)
    data = url_handle.read().decode()
    print('Retrieved:', len(data))
    jsn = json.loads(data)
    for info in jsn['results']:
        print('Place id', info['place_id'])
