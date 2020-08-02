fname = input("Enter file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
# lst = list()
# count = 0
# for line in fh:
#     if not line.startswith("From "):
#         continue
#     lst = line.rstrip().split()
#     print(lst[1])
#     count = count + 1
#
# print("There were", count, "lines in the file with From as the first word")

count = 0
for line in fh:
    line = line.rstrip()
    wds = line.split()
    # guardian
    # if len(wds) < 1: continue
    # if line == '': continue

    # guardian a bit stronger | Pq queeremos imprimir a segunda palavra.
    # Não adianta se não tem a segunda palavra
    # if len(wds) < 2:
    #     continue
    # if wds[0] != 'From':
    #     continue

    # guardian in a compound statement
    # se o primeiro é vdd nem le o segundo
    if len(wds) < 2 or wds[0] != 'From':
        continue
    print(wds[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
