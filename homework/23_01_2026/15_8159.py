def f(x, y, a):
    return (2 * x + y != 150) or (not(50 <= x <= 70)) or (a > y)

for a in range(1, 200):
    if all(f(x, y, a) for x in range(1, 200) for y in range(1, 200)):
        print(a)
        break
# 51