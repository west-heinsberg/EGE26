from itertools import product

cnt = 0

for val in product('012345678', repeat=7):
    val = ''.join(val)
    if val[0] != '0':
        if int(val[0]) % 2 == 0:
            if int(val[-1]) % 3 != 0:
                if '6' in val:
                    cnt += 1

print(cnt)
#827352