fname = input("Enter file: ")
try:
    fh = open(fname)
except:
    print("File cannot be opened", fname)
    quit()

counts = dict()
for line in fh:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    counts[words[1]] = counts.get(words[1], 0) + 1

bigEmail = None
bigCount = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word

print(bigWord, bigCount)
