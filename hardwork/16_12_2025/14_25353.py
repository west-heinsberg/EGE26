from string import printable

def convert(num, sys):
    res = ''
    if num == 0:
        return '0'
    while num != 0:
        res = res + printable[num % sys]
        num = num // sys
    return res[::-1]

ans = []

for x in range(1,27_001):
    z = 3*27**9 + 2*27**6 + 27**3 - x
    z27 = convert(z,27)
    if z27.count('0') == 6:
        ans.append(x)
print(min(ans))
#27