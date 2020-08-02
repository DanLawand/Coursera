# ^	Matches the beginning of a line
# $	Matches the end of the line
# .	Matches any character
# \s	Matches whitespace
# \S	Matches any non-whitespace character
# *	Repeats a character zero or more times
# *?	Repeats a character zero or more times (non-greedy)
# +	Repeats a character one or more times
# +?	Repeats a character one or more times (non-greedy)
# [aeiou]	Matches a single character in the listed set
# [^XYZ]	Matches a single character not in the listed set
# [a-z0-9]	The set of characters can include a range
# (	Indicates where string extraction is to start
# )	Indicates where string extraction is to end


import re

fname = input('Enter file name: ')
hand = open(fname)

numlist = list()
for line in hand:
    line = line.rstrip()
    # stuff = re.findall('[0-9]+', line)
    print(line)
    # for i in stuff:
    #     numlist.append(i)
# print('Soma:', sum(numlist))
print(fim)
