for n in range(1, 1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = '1' + r
        r = r[:-2] + '10'
    else:
        r = r + '1'
        r = '10' + r[2:]
    z = int(r, 2)
    if z > 202:
        print(n)
        break
    #77