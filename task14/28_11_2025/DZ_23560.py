from string import printable
def convert(num,sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]


ans = []
for X in range(1,2401):
    num = 7 * 9 ** 210 + 7 * 9 ** 110 - X
    num9 = convert(num,9)
    if num9.count('0') == 100:
        ans.append(X)

print(max(ans))
#2394