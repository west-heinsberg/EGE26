def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for x in range(1,100_000):
    num = convert(7 ** 666 + 7 ** 333 + 49 ** x - 343, 7)
    if num.count('6') == 49:
        print(x)
        break
# 26
