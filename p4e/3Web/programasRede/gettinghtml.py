import urllib.request, urllib.parse, urllib.error
import re
fhand = urllib.request.urlopen('http://dr-chuck.com/page1.htm')
codigo = list()
for line in fhand:
    linha = line.decode().strip()
    print(linha)
    ref = re.findall('href="(.+)"', linha)
    if len(ref) > 0: codigo.append(ref[0])
print(codigo)
