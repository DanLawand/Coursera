fname = input('Enter file name: ')

try:
    fh = open(fname)
except:
    print('File connot be opened', fname)
    quit()

words = list()
counts = dict()
for line in fh:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

tmp = list()
# for word, count in counts.items():
#         tmp.append((count, word))
# tmp = sorted(tmp)
tmp = sorted([(count, word) for word, count in counts.items()])

for count, word in tmp[:10]:
    print(word, count)
