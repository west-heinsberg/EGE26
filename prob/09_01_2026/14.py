from string import printable
def convert(num,sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []

for x in range(10,70001):
    z = 5**2025 + 5**400 - x
    kek = convert(z,5)
    ans.append([x,kek])
print(ans)