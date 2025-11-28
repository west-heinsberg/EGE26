ans = []

for n in range(1,100_000):
    r = bin(n)[2:]
    if sum(map(int,r)) % 2 == 0:
        r = r + '1'
        r = '11' + r[2:]
    elif r.count('0') > r.count('1'):
        r = r + '0'
    else:
        r = r + '1'
    r = int(r,2)
    if r > 271:
        ans.append(n)
print(min(ans))
#129
