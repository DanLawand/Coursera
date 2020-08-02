# Use urllib para replicar o exercício anterior (1) recu-
# perando um documento de uma URL, (2) mostrando até 3000 caracteres
# e (3) contando o total destes no documento. Não se preocupe sobre os
# cabeçalhos para esse exercício, apenas mostre os 3000 primeiros carac-
# teres do contepudo do documento.
import urllib.request, urllib.parse, urllib.error
url = input('Enter URL: ')
if len(url) < 1:  url = 'http://data.pr4e.org/romeo-full.txt'

try:
    fh = urllib.request.urlopen(url)
except:
    print('Wrong URL')
    quit()
count = 0
doc = list()
for line in fh:
    doc.append(line.decode())
tudo = "".join(doc)
print(tudo[:3000])
print(len(tudo))
