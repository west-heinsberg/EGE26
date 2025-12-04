from itertools import product

count = 1
alph = sorted('АГДИЛНРЯ')

for val in product(alph, repeat=6):
    if count % 2 == 0 and val[0] != 'Я' and val.count('Д') == 3:
        print(count)
    count += 1
# ----