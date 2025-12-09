from itertools import *

cnt = 0
alph = sorted('АВТОР')

for val in product(alph, repeat=4):
    val=''.join(val)
    cnt += 1
    if val[0]=='В' and val[1]=='А' and val[2]=='Т' and val[3]=='А':
        print(cnt)
        break
#146