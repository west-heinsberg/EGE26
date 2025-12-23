from itertools import product

cnt = 0

for val in product('0123456',repeat=7):
    val=''.join(val)
    val=val.replace('4','2').replace('6','2')
    if val[0]!='0':
        if val.count('2') + val.count('0') == 2:
            cnt+=1
print(cnt)
#75816