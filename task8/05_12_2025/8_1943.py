from itertools import product

cnt = 0

for val in product('ЗЕРКАЛО', repeat=6):
    val = ''.join(val)
    if 1 <= val.count('К') <= 4: #проверка что мб еньше четырёх но есть хотябы 1
        val = val.replace('К', '')
        if len(val) == len(set(val)):
        #if val.count("Ц") <= 1: #если ставить == то это счет только если 1 буква но некорр ттк каунтов мб много
            cnt += 1
print(cnt)
