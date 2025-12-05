from itertools import product

cnt = 0

for val in product('ПСКАЛЬ', repeat=4):
    val = ''.join(val)
    if val[0] != "Ь" and 'ЬЬ' not in val: #во всех комбинациях придумать эти комбинации и юзать not in
        cnt += 1
print(cnt)
