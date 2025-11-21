for n in range(3,100_000): # 3 тк 1ой нет, а вторая уже упом
    if 41 % n == 2 and 131 % n == 1:
        print(n)
        break
#13