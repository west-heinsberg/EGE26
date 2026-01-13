from itertools import product, permutations
from string import printable
#
# cnt = 0
#
# for val in product(printable[:9],repeat=7):
#     val = ''.join(val)
#     if val[0] != '0':
#         if val.count('2') == 0 and len(set(val)) == 7:
#             for i in val:
#                 if val[i] % 2 != 0 and val[i + 1] % 2 != 0:
#
#             cnt += 1
# print(cnt)

cnt = 0
for val in permutations(printable[:9], r=7):
    val = ''.join(val)
    if val[0] != '0' and val.count('2') == 0:
        for i in '1357':
            val = val.replace(i, '*')
        for i in '0468':
            val = val.replace(i,'+')
        if '++' not in val and '**' not in val:
            cnt +=1
print(cnt)