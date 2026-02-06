
########################################################################
# Решение в 19: 28

#19:37 дополнили
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def fact(num):
    d = []

    while num % 2 == 0:
        d += [2]
        num //= 2

    i = 3
    while i * i < num:
        while num % i == 0:
            d += [i]
            num //= i
        i += 2

    if num > 2:
        d += [num]

    return d


cnt = 0
for i in range(5_000_00_1, 10 ** 20, 2): # тк стартуем от 5м-ов с шагов 2 чтобы брать нечет (по усл)
    d = fact(i) # выписали факт в переменную
    if len(d) == len(set(d)) == 2 and is_prime(abs(d[1] - d[0])): # упростили проверку 19:34 + нечёт числа на 2 не делятся
        print(i, d[1])
        cnt += 1
        if cnt == 5:
            break