from string import printable
def convert(num,sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []

for n in range(1,100_000):
    r = convert(n,3)
    sum_3 = sum(map(lambda x: int(x, 3), r))
    if sum_3 % 2 == 0:
        r = '1' + r + '2'
    else:
        r = '2' + r + '0'
    r = int(r,3)
    if r > 100:
        ans.append(r)
print(min(ans))