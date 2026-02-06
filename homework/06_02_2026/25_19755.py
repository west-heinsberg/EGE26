def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            d.append(i)
            if i != num // i:
                d.append(num // i)

    p = []
    for x in d:
        if is_prime(x):
            p.append(x)

    if len(p) > 0:
        p.sort()
        m_val = p[0] + p[-1]
        return m_val
    return 0


cnt = 0
for N in range(1_200_001, 2_000_000):
    M = f(N)
    if M > 2000 and M % 10 == 8:
        print(N, M)
        cnt += 1
        if cnt == 5:
            break