# Goal: to extract certain part of the data in a geolocation open API ie., lon,lat, plus code


import urllib.request, urllib.parse
import json, ssl

FXDURL = "https://py4e-data.dr-chuck.net/opengeo?"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#URL = input("Enter url: ")
#uh = urllib.request.urlopen(URL, context=ctx)
#data = uh.read().decode()

while True:
    loc = input("Enter Location: ")
    if len(loc) < 1:
        break

    loc = loc.rstrip()
    cndt = dict()
    cndt['q'] = loc

    url = FXDURL + urllib.parse.urlencode(cndt)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    #print('Retrieving: ', data)


    js = json.loads(data)

    
    xtract = (json.dumps(js['features'][0]['properties'], indent=4))   #indent to see via pretty print, and using dumps makes use store JSON data directly into a file. Use this to access the tree.


    print ('Extracted: ', xtract)