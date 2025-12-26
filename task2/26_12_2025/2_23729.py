from itertools import product, permutations

def f(x, y, z, w):
    return (x or y) and not (y == z) and not w

for i in product((0, 1), repeat = 4): # принимает кортеж из 0 и 1, 4 - т.к. пустые ячейки
    table = [ # строки храним в виде кортежей
        (1, i[0], 1, i[1]),
        (0, 1, i[2], 0),
        (i[3], 1, 1, 0)
    ]

########################## ИЛИ
# for a1, a2, a3, a4 in product((0,1),repeat = 4 )
    # дальше соотв. расставл.

# в табле три лемента - эти кортежи, нуно проверить их уникальность
    if len(set(table)) == len(table):
        for p in permutations('xyzw'): # заголовки
            # zip(p, t) - сопоставляет заголовки из p c значениями из t;
            # dict(zip(p, t)) - преобразует zip объект в базовый тип данных (словарь);
            # f(**dict(zip(p, t))) - распаковывает через kwargs все ключи в функцию;
            if [f(**dict(zip(p,t))) for t in table] == [1, 1, 1]: # из табл извлекаем 1ю строчку и прим переставку п, единицы потому что f == 1
                print(*p, sep='') # сеп от принта, separate, разделитель, в даном случае склеит.