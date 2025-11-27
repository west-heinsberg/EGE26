for n in range(1,100_000):
    r = bin(n)[2:]
    if n % 2 == 0:
        z1 = r.count('1')
        z2 = bin(z1)[2:]
        r = r + z2
    else:
        r = '1' + r + '101'
    r = int(r,2)
    if r > 350:
        print(n)
        break
#17