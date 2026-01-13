from string import printable
from itertools import permutations

cnt = 0

for val in permutations(printable[:8], r=6):
    if '3' in val:
        continue
    if val[0] == '0':
        continue
    if any(int(val[i]) % 2 == 0 and int(val[i+1]) % 2 == 0 for i in range(5)):
        cnt += 1

print(cnt)

#3852