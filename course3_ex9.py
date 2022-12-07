import urllib.request, urllib.parse, urllib.error
import json


serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('Enter location:')
    if len(address) < 1:
        break
    key_api = 42

    url = serviceurl + urllib.parse.urlencode({'address' : address, 'key': key_api}) 

    print('Retrieving',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data),'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure To Retrieve ===')
        print(data)
        continue
    
    place_id = js["results"][0]["place_id"]
    print('Place id',place_id)



