from itertools import product

alph = sorted(set('СУБЛИМАЦИЯ'))
cnt = 0

for pos, val in enumerate(product(alph, repeat=5), start=1):
    if pos % 2 != 0:
        if val[-1] != 'Я':
            if val.count('А') + val.count('И') + val.count('У') + val.count('Я') == 2:
                cnt = pos

print(cnt)

#58955