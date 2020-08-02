fname = input('Enter file name: ')
if len(fname) < 1 : fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print('File connot be opened', fname)
    quit()

words = list()
counts = dict()
for line in fh:
    words = line.split()
    if len(words) < 6 or words[0] != 'From':
        continue
    hour = words[5].split(':')
    counts[hour[0]] = counts.get(hour[0], 0) + 1

tmp = sorted([(word, count) for word, count in counts.items()])

for word, count in tmp:
    print(word, count)
