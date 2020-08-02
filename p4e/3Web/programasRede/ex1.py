# Altere o programa de soquete socket1.py pR pedir ao
# usuário a URL para que então possa ler qualquer página da web.Você
# pode usar split('/') para quebrar a URL em suas componentes para
# que então possa extrair o nome do hospedeiro para que o soquete connect
# chame. Adicione tratamento de erro usando try e except para lidar com
# a condição do usuário digitar uma URL formatada incorretamente ou
# uma não existente

import socket

url = input('Enter url: ')
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

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()
