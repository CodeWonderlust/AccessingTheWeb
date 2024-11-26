import urllib.request, urllib.parse
import json, ssl

#url = 'http://py4e-data.dr-chuck.net/comments_42.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


URL = input('Enter url: ')

uh = urllib.request.urlopen(URL, context=ctx)
data = uh.read().decode()
js = json.loads(data) #purpose of this is to parse a valid JSON string and convert it into a python dictionary. Hence you only "print (data)" it will only show the actual data on the web.

#print (js)

tcount = 0
tsum = 0

for _ in js['comments']:
    tcount = tcount + 1
    tsum += int(_['count'])

print ('Total Count: ', tcount)
print ('Total Sum: ', tsum)