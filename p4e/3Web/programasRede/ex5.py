import socket
url = input('Enter URL: ')
if len(url) < 1: url = 'http://data.pr4e.org/romeo.txt'
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = url.split('/')
str = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
try:
    mysock.connect((host[2], 80))
    cmd = str.encode()
    mysock.send(cmd)
except:
    print('wrong url')
    quit()


resp = []
while True:
      data = mysock.recv(200)
      if not data: break
      resp.append(data.decode())
mysock.close()

# Vira tudo uma string
resp = "".join(resp)
tudo = resp.split('\r\n\r\n')
# Isso significa que eu quero o segundo termo do array que resp.split() retorna
# body = resp.split('\r\n\r\n')[1]
header = tudo[0]
body = tudo[1]
print(body)
