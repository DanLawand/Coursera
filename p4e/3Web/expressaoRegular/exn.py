import re

fname = 'regex_sum_800030.txt'
hand = open(fname)

numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+', line)
    print(line)
    for i in stuff:
        num = int(i)
        numlist.append(num)
print(sum(numlist))
