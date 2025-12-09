from itertools import product
from string import printable

for val in product(printable[:15], repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1:
        # cnt = 0
        # for i in val:
        #     if int(i,15) > 9:
        #         cnt_9 += 1
        # далее методы списочных вложений
        if len([i for i in val if int(i,15) > 9]) >= 2:
        #если непом лен
        # if [1 for i in val if int(i, 15) > 9].count(1) >= 2:
        # мат фуннкцией без каунт и лен: if sum([1 for i in val if int(i,15) > 9]) >= 2:
        # if sum[val.count(i) for i in printable[10:15]] >= 2:
        cnt += 1
print(cnt)

#################################################
# учит запись
from itertools import product
from string import printable

cnt = 0
for val in product(printable[:15], repeat=5): # 00010
    val = ''.join(val)
    if val[0] != '0' and val.count('8') == 1:
        if len([i for i in val if int(i, 15) > 9]) >= 2:
            if [1 for i in val if int(i, 15) > 9].count(1) >= 2:
                if sum([1 for i in val if int(i, 15) > 9]) >= 2:
                    if sum([val.count(i) for i in printable[10:15]]) >= 2:
                        cnt += 1

print(cnt)


