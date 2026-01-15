from itertools import product
from string import printable

cnt = 0
for val in product(printable[:6], repeat = 7):
    val = ''.join(val)
    if val[0] != '0' and val.count('2') == 1:
        for z in '04':
            val = val.replace(z, 'Ч')
        if '2Ч' not in val and 'Ч2' not in val:
            cnt += 1
print(cnt)
# 40500