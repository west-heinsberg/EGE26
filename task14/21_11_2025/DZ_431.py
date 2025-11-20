for x in range(1, 1000):
    num = 3 * 7**(x+1) + 13 * 7**(x+2) + 31 * 7**(3*x) + 1 * 7**(2*x)
    sum1 = 0
    num7 = num
    while num7 > 0:
        sum1 += num7 % 7
        num7 //= 7
    if sum1 == 18:
        print(x)
        break
#3