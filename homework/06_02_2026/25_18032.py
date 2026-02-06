def f(num):
    summ = 0
    for i in range(1, num + 1):
        if num % i == 0:
            summ += i
    return summ


cnt = 0
for N in range(1000, 10000):
    M = f(N)
    if M % 100 == 23:
        print(N, M)