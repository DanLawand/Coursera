import re
hand = open('mbox-short.txt')

numlist = list()
for line in hand:
    line = line.rstrip()
    # [0-9.+] parece que vai retornar 0.1.9.3.3 coisas assim
    # ('^X-DSPAM-Confidence: ([0-9].[0-9]+)', line) => evita coisas como 0.986sd
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9].+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
