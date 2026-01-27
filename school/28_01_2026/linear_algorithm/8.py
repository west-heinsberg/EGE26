x = int(input())
c = (x % 10 % 2) + (x // 10 % 10 % 2) + (x // 100 % 2)
print(c)