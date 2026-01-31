from itertools import product

alph = sorted('ПАРУС')

for pos, val in enumerate(product(alph,repeat=5),start=1):
    val = ''.join(val)
    if val.count('У') <= 1:
        if 'АА' not in val:
            print(pos, val)
            break

# 131 АПАПА