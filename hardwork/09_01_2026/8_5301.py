from itertools import product

cnt = 0

for val in product('ЛЕСЯ_',repeat=5):
    val = ''.join(val)
    if 'ЕЯ' not in val or 'ЯЯ' not in val or 'EE' not in val or 'ЕЕ' not in val:
        if 'ЛС' not in val or 'СС' not in val or 'ЛЛ' not in val or 'СЛ' not in val:
            if val[4] != '_' and val[0] != '_':
                if val.count('_') == 1:
                    cnt += 1
print(cnt)

