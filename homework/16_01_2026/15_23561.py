def f(x):
    return (x % 128 == 0) <= ((x % a != 0) <= (x % 80 != 0))

for a in range(1,1000)[::-1]:
    if all(f(x) == 1 for x in range(1,1000)):
        print(a)
        break

# 640