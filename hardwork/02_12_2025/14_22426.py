def convert(num, sys):
    res = ''
    while num != 0:
        res = res + str(num % sys)
        num = num // sys
    return res[::-1]


x = 15 * 343**2031 + 7 * 49**1142 - 3*7**111 + 7**222 - 16809
