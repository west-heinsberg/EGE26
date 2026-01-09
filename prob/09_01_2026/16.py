def F(n):
    for n in range(1,100000):
        if n == 1:
            return 1
        if n > 1:
            return 2 * F(n-1)