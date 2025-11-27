for x in range(2,3001):
    num = 9 * 11**210 + 8*11**150 - x
    count = 0
    while num > 0:
        if num % 11 == 0:
            count += 1
            num //= 11
    if count == 60:
        print(x)
        break
#не выполняется