# дел можно в свою ф-ю
# def DEL(n,m):
#     return n % m == 0


def f(x):
    return ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80)

for A in range(-1000,1000): # срез убир тк наименьш // убираем 'y' тк нет в задаче
    if all(f(x) for x in range(1,1000)):
        print(A)
        break