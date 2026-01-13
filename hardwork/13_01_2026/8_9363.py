from itertools import permutations

cnt = 0
alph = 'Х*Ч*Н*Б*ДЖ*Т'

for val in permutations(alph):
    val = ''.join(val)
    if '*****' not in val:
        cnt +=1
print(cnt)