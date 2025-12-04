from itertools import product

count = 0

alph = sorted('ДЖОС')

for val in product(alph, repeat = 6):
   count += 1
   val = ''.join(val)
   if val[0] + val[1] == 'ЖС':
       print(count)
       break