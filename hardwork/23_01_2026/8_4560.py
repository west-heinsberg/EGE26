from itertools import product

alph = 'ТИХОРЕЦК'
cnt = 0

for val in product(alph,repeat=4):
    val = ''.join(val)
    cnt_tiho = 0
    for i in range(4): # 4 позиции, это и ниже можно реализовать через СВ
        # if val[i] == 'ТИХО'[i]:
        #     cnt_tiho += 1
    if len(set(val)) == 4:
        if val.count('И') + val.count('О') + val.count('E') == 2:
            # if len(['k' for i in range(4) if val[i] == 'ТИХО'[i]]) == 2 and val.count('*') == 2:
            # или if sum([1 for i in range(4) if val[i] == 'ТИХО'[i]]) == 2 and val.count('*') == 2:
            # или изич: if sum(val[i] == 'ТИХО' //
            # for i in "ИОЕ":
            #   val = val.replace(i,'*')
            #   if cnt_tiho == 2 and val.count('*') == 2:
            #   cnt += 1
x
            #   cnt += 1

                cnt += 1

print(cnt)