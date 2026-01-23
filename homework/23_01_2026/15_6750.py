def f(x, y, a):
    return (x + y <= 32) or (y <= x + 4) or (y >= a)

for a in range(100, -1, -1):
    if all(f(x, y, a) for x in range(1, 100) for y in range(1, 100)):
        print(a)
        break
# 19