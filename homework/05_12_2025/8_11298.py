from itertools import product

count = 0
count1 = 0

alph = sorted('АЖЗОПЮ')

for val in product(alph, repeat = 6):
   count += 1
   val = ''.join(val)
   if count % 2 == 0 and val[0] == 'А' and val.count('З') >= 2:
       count1 += 1
print(count1)
#513