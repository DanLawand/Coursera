import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://dr-chuck.com'
# .read() transforma tudo numa string sem a quebra de linha
html = urllib.request.urlopen(url).read()
# vai separar de maneira bonitinha o html
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
