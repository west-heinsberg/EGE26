from string import printable as alph # подключаем символы

from task5.theory import num_2

for x in alph[:19]: #срез для 19 СС, можно провер с помощью 10 СС и 2 СС
    num_1 = int(f'98{x}79641', 19) # подставляем в ф строку, ф строка тк форматирумая и указываем СС + уч что инт приним только строки
    num_2 = int(f'36{x}14',19) # следить чтобы написал 19 обязательно
    num_3 = int(f'73{x}4',19)
    num = num_1 + num_2 + num_3
    if num % 18 == 0:
        print(x, num // 18)