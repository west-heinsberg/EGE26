from itertools import product
from string import printable

cnt = 0

for val in product(printable[:8],repeat=6):
    if val[0] != '0' and len(set(val)) == len(val) and int(val,8) % 5 == 0:
            for i in val:
                if int(i) % 2 == 0:
                    val = val.replace(i,'*')
                else:
                    val = val.replace(i,'+')
            if '**' not in val and '++' not in val:
                cnt += 1
print(cnt)
