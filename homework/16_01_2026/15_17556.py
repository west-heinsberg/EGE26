def DEL(n,m):
    return n % m == 0

def f(x):
    return (x % A == 0) or ((70 <= x <= 90) <= (x % 22 != 0)) # АЛЬТЕРНАТИВНАЯ ЗАПИСЬ Б -- or ((x in range(70,91))

for A in range(1,1000)[::-1]:
    if all(f(x) for x in range(1,1000)):
        print(A)
        break

# 88