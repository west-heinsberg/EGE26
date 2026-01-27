x = int(input())
p = (x % 10) * (x // 10 % 10) * (x // 100 % 10) * (x // 1000)
print(p)