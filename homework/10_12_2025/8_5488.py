from itertools import product

cnt = 0

for val in product('ПОЛИНА',repeat=8):
    val = ''.join(val)
    if val.count('П') + val.count('Л') + val.count('Н') > 4:
        cnt += 1
print(cnt)

#610173