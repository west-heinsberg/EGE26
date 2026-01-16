ans = []
from string import printable
def convert(num,sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

for n in range(1,100_100):
    r = f'{n:o}'
    if r[0] == '5':
        r = r.replace('2','*')
        r = r.replace('1','2')
        r = r.replace('*','1')
        r = '11' + r
    else:
        r = r + '10'
        r = '2' + r[1:]
    r = int(r,8)
    if r < 1354:
        ans.append([r,n])

print(max(ans))

# 61

