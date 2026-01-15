from itertools import product
from string import printable

cnt = 0

for val in product(printable[:16], repeat = 4):
    val = ''.join(val)
    if val[0] != '0' and val.count('9') == 1:
        for z in '02468ace':
            val = val.replace(z, 'Ч')
        for z in '13579bdf':
            val = val.replace(z, 'Н')
        if 'НН' not in val and 'ЧЧ' not in val:
            cnt += 1
print(cnt)
# 1680