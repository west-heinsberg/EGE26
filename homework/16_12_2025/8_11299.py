from itertools import product

cnt = 0
alph = sorted('БМЮРН')

for val in product(alph, repeat = 6):
   cnt += 1
   val = ''.join(val)
   if cnt % 2 != 0 and val[0] != 'М':
       if val.count('Р') >= 2 and 'Ю' not in val:
           print(cnt)
#11719