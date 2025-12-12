from itertools import permutations
from string import printable # тк здесь шестизнач дес числа

cnt = 0
for val in set(permutations(printable[:10],r=6)): # r = 6 тк шестизначные числа
    val = ''.join(val)
    if val[0] != '0' and int(val) % 4 == 0:
        for i in '02468':                         # 0 ЧЕТНЫЙ!!!!!!!!!!!!!!!!!!!!!!!!!!
            val = val.replace(i, '*')
        if '**' not in val:
            cnt += 1
print(cnt)
#7440
