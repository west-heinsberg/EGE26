def f(x, y, z):
    return (x | 50 == x) or (y & 34 != 0) or (z | 24 != 24) or (x * y * z > a // 8) # | побитовое деление


for a in range(1, 1000)[::-1]:
    if all(f(x, y, z) for x in range(1, 100) for y in range(1, 100) for z in range(1, 100)):  # перебираем возможные икс и проверяем чтобы ответ не менялся учитывая время
        print(a)
        break
