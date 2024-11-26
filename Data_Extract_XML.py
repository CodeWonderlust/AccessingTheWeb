import urllib
import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter URL: ")
uh = urllib.request.urlopen(url)
data = uh.read()

mt = ET.fromstring(data)
xtrct = mt.findall("comments/comment")

count = 0
sum = 0

for i in xtrct:
    x = int(i.find("count").text)
    count = count + 1
    sum = sum + x

print ("Count: ", count)
print ("Sum: ", sum)


#Link
#  http://py4e-data.dr-chuck.net/comments_42.xml