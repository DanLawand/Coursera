# Altere o programa urllinks.py para extrair e contar as
# tags de parágrafos (p) do documento de HTML recuperado e mostrar a
# contagem dos parágrafos como uma saída do seu programa.Não mostre
# o conteúdo, apenas conte-os. Teste seu programa em várias páginas da
# web pequenas e também em algumas maiores.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1: url = 'http://www.dr-chuck.com/page1.htm'
try:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
except:
    print('Wrong URL')
    quit()
# Retrieve all of the anchor tags
tags = soup('p')
i = 0
for tag in tags:
    i = i + 1
print(i)
