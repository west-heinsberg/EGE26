from itertools import product

n = 0
cnt = 0

for val in product('ПРЕСТОЛ',repeat=5):
    val = ''.join(val)
    n += 1
    if n % 2 == 1 and val[-1] in 'ЕО':
         a = 0
         for j in 'ЛПРСТ':
            a += val.count(j)
         if a <= 3:
            cnt += 1
print(cnt)


#1776