from itertools import product

cnt = 0

for val in product('10', repeat=16):
    val = ''.join(val)
    if val.count('1') % 3 == 0 and val[0] != '0':
        cnt += 1
print(cnt)

#10923