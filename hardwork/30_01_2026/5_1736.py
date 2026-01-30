ans = []
for n in range(1,100_000):
    r = f'{n:b}'
    r = r.replace('0','00')
    r = r.replace('1','11')
    r = int(r,2)
    if r > 63:
        ans.append(r)

print(min(ans))
# 193

# 2 сп .. // без реплейсов
ans = []
for n in range(1,100000):
    r = list(f'{n:b}')
    for i in range(len(r)):
        r[i] = r[i] * 2
    r = int(''.join(r),2)
    if r > 63:
        ans.append(r)
print(min(ans))