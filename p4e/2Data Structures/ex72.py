fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
dspam = 0
avg = 0
v = 'X-DSPAM-Confidence: '

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    try:
        dspam = float(line[len(v):])
    except:
        print('Conversion cannot be happened:', line[len(v):])
        quit()
    print(line)
    avg = avg + dspam
    count = count + 1

print('Average spam confidence:', avg/count)
