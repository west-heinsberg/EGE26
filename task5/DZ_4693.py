for n in range(0, 200):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r + '0'
        r = '10' + r[2:]
    else:
        r = r + '1'
        r = '11' + r[2:]
    z = int(r, 2)
    if z > 40:
        print(n)
        break
#16