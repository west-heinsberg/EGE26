from itertools import permutations

cnt = 0

for val in set(permutations('АМФИБРАХИЙ')):
    val = ''.join(val)
    if 'ААФИИ' in val or 'ИИФАА' in val:
        cnt += 1
print(cnt)
#1440