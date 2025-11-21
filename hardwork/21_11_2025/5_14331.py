from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []

for n in range(1,100_000):
    r = convert(n, 3)
    sum_1 = sum(map(lambda x: int(x,36), r))
    if sum_1 % 3 == 0:
        r += '212'
    else:
        sum_1 = sum_1 * 2
        t = convert(sum_1,3)
        r = r + t
    r = int(r,3)
    if r > 490:
        ans.append(r)
print(min(ans))