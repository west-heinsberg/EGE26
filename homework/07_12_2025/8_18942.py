from itertools import product

cnt = 0
alph = sorted('ДИОНИСИЙ')

for val in product(alph,repeat=6):
    val = ''.join(val)
    if ('Д' in val and 'Н' not in val) or ("Н" in val and "Д" not in val):
