from itertools import permutations

cnt = 0

for val in set(permutations('СОРТИРОВКА')):
    val = ''.join(val)
    val = val.replace('А','*').replace('И','*').replace('О','*')
    val = val.replace('С','?').replace('Р','?').replace('Т','?').replace('В','?').replace('К','?')
    if '***' not in val and '???' not in val:
        cnt += 1
print(cnt)
#185760