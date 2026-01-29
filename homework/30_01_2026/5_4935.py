ans = []

for n in range(1,30):
    r = f'{n:b}'
    if r.count('1') % 2 == 0:
        r = '10' + r
        r = r[:-2] + '00'
    else:
        r = '11' + r
        r = r[:-2] + '11'
    r = int(r,2)
    ans.append(r)

print(max(ans))
# 127