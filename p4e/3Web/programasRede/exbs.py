import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
position = input('Enter position: ')

try:
    contador = int(count)
    posicao = int(position)
except:
    print('Wrong input')
    quit()
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print('Retrieving:', url)

pos = 0
i = 0
for i in range(contador):
    tags = soup('a')
    for tag in tags:
        if pos == posicao-1:
            url = tag.get('href', None)
            break
        pos = pos + 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print('Retrieving:', url)
    pos = 0
name = re.findall('known_by_(.+)\.html', url)
print(name[0])
