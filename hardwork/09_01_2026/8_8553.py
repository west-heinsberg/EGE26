from itertools import product

alph = sorted('НОРМАЛЬЕ')

ans = []

for pos, val in enumerate(product(alph,repeat=6),start=1):
    val = ''.join(val)
    if val[:4] == 'НОРМ':

    if val [:6] == 'НЕНОРМ'
    ans.append(val)


print(ans)
