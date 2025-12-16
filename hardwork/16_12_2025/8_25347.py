from itertools import product

alph = sorted('ГРАНИТ')
cnt = 0

for pos, val in enumerate(product(alph,repeat=6),start=1):
    val = ''.join(val)
    if val[0] not in 'АИГ' and val.count('А') == 1:
        cnt += 1
        print(pos, val)
#23589