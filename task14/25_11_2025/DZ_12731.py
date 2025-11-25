from string import printable as alph
for x in alph[1:13]: # СТАВИМ 1 ТК ИНАЧЕ ПОЛУЧАЕТСЯ НЕЗНАЧ НОЛЬ, Х = 0 В ОТСЧЕТ НЕ БЕРЁМ
    num_1 = int(f'9{x}AB', 13)
    num_2 = int(f'{x}46C', 16)
    num_3 = int(f'B7{x}', 15)
    num = num_1 + num_2 - num_3
    if num % 14 == 0:
        print(x, num // 14)