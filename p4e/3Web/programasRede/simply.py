import urllib.request, urllib.parse, urllib.error
HOST = 'http://data.pr4e.org/romeo.txt'
fhand = urllib.request.urlopen(HOST)
for line in fhand:
    print(line.decode().strip())
