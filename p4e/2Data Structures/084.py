fname = input('Enter file name: ')

try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

lst = list()
words = list()
for line in fh:
    words = line.split()
    for i in range(len(words)):
        if words[i] not in lst:
            lst.append(words[i])
lst.sort()
print(lst)
