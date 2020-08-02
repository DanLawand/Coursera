data  = 'ola meu email é daniel.lawand@usp.br Sábado dia 9'

atpos = data.find('@')
print(atpos)

#            find(char, início)
sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)
