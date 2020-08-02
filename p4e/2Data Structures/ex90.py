fname = input('Enter the file name: ')

try:
    fh = open(fname)
except:
    print("File cannot be opened", fname)
    quit()

counts = dict()
# Conta qual palavra tem mais frequência
for line in fh:
    # line.strip() split faz o strip
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Armazena a palavra de maior frequência e a sua quantidade
bigCount = None
bigWord = None
for word,count in counts.items():
    # Se é o primeiro loop ou se não é a palavra de maior frequência, então (remember):
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word

print(bigWord, bigCount)
