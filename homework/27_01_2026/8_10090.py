from itertools import permutations

cnt = 0

for val in permutations('0234567',r=5):
    val = ''.join(val)
    if val[0] != '0':
            val = val.replace('2','*').replace('4','*').replace('6','*').replace('0','*')
            val = val.replace('3','+').replace('5','+').replace('7','+')
            if '++' not in val and '**' not in val:
                cnt += 1

print(cnt)
# 180