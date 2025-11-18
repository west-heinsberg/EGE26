ans = []
for n in range(0,100_000):
    r = bin(n)
    if n % 8 == 0:
        r = r + r[-2:]
    else:
