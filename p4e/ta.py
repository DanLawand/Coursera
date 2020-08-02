def main():
    fname = input('Enter File Name: ')
    if len(fname) < 1: fname = 'abcd.txt'
    try:
        fh = open(fname)
    except:
        print('Wrong file')
        quit()
    i = 1
    for line in fh:
        lst = line.strip().split()
        a = int(lst[0])
        b = int(lst[1])
        c = int(lst[2])
        d = int(lst[3])
        if c < d:
            t = d
            d = c
            c = t
        if d < a:
            t = a
            a = d
            d = t
        if a > b:
            t = a
            a = b
            b = t
        if c < b:
            t = c
            c = b
            b = t
        if d < c:
            t = d
            d = c
            c = t
        if a<=b and b<=c and c<=d:
            print(i, ' True: ', a, b, c, d)
        else:
            print(i, ' False: ', a, b, c, d)
        i = i + 1
main()
