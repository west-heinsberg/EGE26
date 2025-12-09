from string import printable

def convert(num,sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []
for n in range(1,100_000):
    r_9 = convert(n,9)
    if r_9[0] == '7':
        r_9 = r_9.replace('6','*')
        r_9 = r_9.replace('3','6')
        r_9 = r_9.replace('*','3')
        r_9 = '34' + r_9
    else:
        r_9 = r_9 + '45'
        r_9 = r_9[0] + '3'
    r_9 = int(r_9, 9)
    if r_9 < 2876:
        ans.append([r_9,n])
a = max(ans)
res = []
for i in range(len(ans)):
    if ans[i][0] == a[0]:
        res.append(ans[i][1])
print(max(res))