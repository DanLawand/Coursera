# Altere seu programa de soquete para que ele conte o
# número de caracteres que recebeu e pare de mostrar qualquer texto
# depois que mostrar 3000 caracteres. O programa deve recuperar o doc-
# umento inteiro e contar o número total de caracteres e mostrar o resul-
# tado da contagem no final do documento.
import socket
import time
url = input('Enter URL: ')
if len(url) < 1: url = 'http://data.pr4e.org/romeo-full.txt'
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = url.split('/')
str = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
try:
    mysock.connect((host[2], 80))
    cmd = str.encode()
    mysock.send(cmd)
except:
    print('Wrong URL')
    quit()

contador = 0
doc = list()
while True:
    data = mysock.recv(500)
    contador = contador + len(data)
    if len(data) <= 0 :
        break
    # if contador <= 3000:
        # print(data.decode(),end='')
    doc.append(data.decode())
    time.sleep(0.1)
mysock.close()

tudo = "".join(doc)
resp = tudo.split('\r\n\r\n')
# Isso significa que eu quero o segundo termo do array que resp.split() retorna
# body = resp.split('\r\n\r\n')[1]
header = resp[0]
body = resp[1]
print(body[:3000])
print(len(body))
