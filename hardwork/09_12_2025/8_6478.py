from itertools import product

cnt = 0
alph = sorted('МОЛЬ')

for val in product(alph,repeat=5):
    val = ''.join(val)
    if 'МЬ' or 'ЛЬ' in pos:
        cnt +=1
print(cnt)

##############################

cnt1 = 0

for val in product(sorted('МОЛЬ'),repeat=5):
    val = ''.join(val) # обязательно соединяем тк ищем буквы
    if 'ОЬ' not in val and  'ЬЬ' not in val and val[0] != 'Ь':
        cnt1 += 1
print(cnt1)