def convert(num, sys):
    # if num == 0: return 0
    res = ''
    while num > 0:
        res = res + str(num % sys)
        num = num // sys
    return res[::-1] if res else '0'

ans = []

for n in range(0,100_000):
    r = convert(n,4)
    if n % 2 == 0:
        r = '12' + r + convert(int(r[-1]) * 3,4)
    else:
        r = '13' + r + '21'
    r = int(r,4)
    if r > 50:
        ans.append(r)
print(min(ans))

# 96