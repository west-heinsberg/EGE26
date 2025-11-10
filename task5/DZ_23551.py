for n in range(1, 100):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    z = int(r, 2)
    if z < 30:
        print(n)
#6