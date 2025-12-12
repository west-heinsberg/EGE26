from itertools import product
from string import  printable

cnt = 0

for val in product(printable[:12],repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        new_v = ''
        for i in val:
            if int(i,12) % 3 == 0:
                new_v += '*'
            else:
                new_v += '+'
        if '**' not in new_v or '++' not in new_v:
            cnt += 1
print(cnt)