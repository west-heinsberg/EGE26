from itertools import *

cnt = 0
alph = sorted('ПАРУС')

for val in product(alph,repeat=5):
    val = ''.join(val)
    cnt += 1
    if val[0] == 'У' and 'АА' not in val:
        print(cnt)
        break
#2527