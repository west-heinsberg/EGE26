ans = []
def convert(num,sys):
    res = ''
    while num:
        res += num + str(num % sys)
        num //= sys
    return res[::-1]

for n in range(1,100_000):
    r = convert(n,4)
    if sum(map(int(r,4))) % 3 == 0:
        r = r.replace('0', '*').replace('2', '0').replace('*', '2')
        r = '32' + r
    else:
        r += '33'
        r = r[0] + '10' + r[3:]
r10 = int(r, 4)
print(r10)
#неуд
