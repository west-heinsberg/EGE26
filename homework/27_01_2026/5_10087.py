ans = []

for n in range(1,100_000):
    r = f'{n:b}'
    if n % 3 == 0:
        r += r[-3:]
    else:
        ost = 3*(n % 3)
        ost = f'{ost:b}'
        r = r + ost
        r = int(r,2)
        if r > 151:
            ans.append(r)

print(min(ans))

# 163