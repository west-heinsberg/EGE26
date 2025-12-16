def convert(num, sys):
    res = ''
    if num == 0:
        return '0'
    while num != 0:
        res = res + str(num % sys)
        num = num // sys
    return res[::-1]

ans = []
for n in range(1,100_000):
    r = convert(n,3)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        sumr = sum(map(int, r))
        sumr = sumr * 3
        sumr3 = convert(sumr,3)
        r = r + sumr3
    r = int(r,3)
    if r > 208 and r % 2 != 0:
        ans.append(r)
print(min(ans))

#243