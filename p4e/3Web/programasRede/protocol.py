import socket
# Retorna um objeto
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect method no objeto. E passamos o host que nos queremos
# nos conectar (domain) e o 'port' que nós queremos nos conectar
mysock.connect(('data.pr4e.org', 80))

# encode == trasnforma UNICODE  em UTF-8.
cmd = 'GET http://http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    # data = recebe 512 caracteres
    data = mysock.recv(512)
    # Se não receber nenhum dado
    # Fim do arquivo ou fim da transmissão
    if (len(data) < 1):
        break
    print(data.decode(),end='')
mysock.close()
