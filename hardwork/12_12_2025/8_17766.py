from itertools import product

alph = sorted('СЕНТЯБРЬ')
cnt = 0

for pos, val in enumerate(product(alph,repeat=5),start=1):
    val = ''.join(val)
    if val[0] == 'Р' and val.count('Ь') == 0:
        print(pos)
#16384