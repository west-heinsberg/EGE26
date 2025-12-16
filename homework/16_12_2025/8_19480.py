from itertools import permutations

cnt = 0

for val in set(permutations('ПАРИЖАНКА')):
    val = ''.join(val)
    val = val.replace('А','*')
    val = val.replace('И','*')
    if val.count('**') == 1 and '***' not in val:
        cnt += 1
print(cnt)



#28800