def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1): # по усл число не дел на 1 и на себя
        if num % i == 0:
            d |= {i, num // i}

    for i in sorted(d):
        if i % 10 == 9 and i != 9:
            return i
    return 0

cnt = 0
for N in range(800_001, 10 ** 20): # 800_001 потому что идем строго от числа
    M = f(N)
    if M % 10 == 9:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break
