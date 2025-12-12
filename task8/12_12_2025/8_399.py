from itertools import permutations

cnt = 0

for val in set(permutations('ВОРОТА',r=6)): # если указана перестановкав задании то пишем полный алфавит если нужен другая длина то r
    val = ''.join(val)                             # СЕТ писать всегда чтобы убрать одинаковые слова (типа ВОРОТА и ВОРОТА, где о - 2)
    if 'ОА' not in val and 'АО' not in val and 'ОО' not in val and 'АА' not in val:
        cnt += 1
print(cnt)