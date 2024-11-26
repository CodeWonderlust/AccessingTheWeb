import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()
for line in fhand:
    words = line.decode().split()
    for _ in words:
        counts[_] = counts.get(_, 0) + 1
print(counts)
