fname = input('Enter Filename: ')
if len(fname) < 1: fname = 'romeo.txt'
try:
    fh = open(fname)
except:
    print('wrong filename')
    quit()
count = 0
for line in fh:
    print(line)
    print(len(line))
    count = count + len(line)
print(count)
