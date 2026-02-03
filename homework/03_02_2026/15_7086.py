def f(x):
    return (x % a == 0) or ((50 <= x <= 70) <= (x % 16 != 0))

for a in range(1,100_000):
    if all(f(x) == 1 for x in range(1,1000)):
        print(a)
# 64