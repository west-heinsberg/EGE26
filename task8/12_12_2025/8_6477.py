from itertools import permutations

cnt = 0
for val in set(permutations('ЛЕВИОСА')):
    val = ''.join(val)
    if val[0] not in 'ЕИОА' and val[3] not in 'ЛВС':
        #..and val[len(val // 2)] проверяем так середину
        cnt += 1
print(cnt)
