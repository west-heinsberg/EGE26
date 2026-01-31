from  itertools import product

cnt = 0

for val in product('М*СЛ*', repeat=6):
    if val.count('*') == 1:
        cnt += 1

print(cnt)
# 2916