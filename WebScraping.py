import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

                                                                    # Retrieve all of the anchor tags
count = 0
sum = 0

tags = soup('span')
for tag in tags:
                                                                    # Look at the parts of a tag
   print ('TAG:',tag)
   x=int(tag.text)            # Converting the string into an integer adding .text to make an HTML file readable
   count = count+1
   sum = sum + x

#   print ('URL:',tag.get('href', None))
#   print ('Contents:',tag.contents[0])
#   print ('Attrs:',tag.attrs)

print (count)
print (sum)

#http://py4e-data.dr-chuck.net/comments_1780900.html 