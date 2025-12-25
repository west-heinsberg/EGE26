def convert(num, sys):
    res = ''
    while num != 0:
        res = res + str(num % sys)
        num = num // sys
    return res[::-1]

x = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
x = convert(x, 5)
x = x.count('0')
print(x)
#38