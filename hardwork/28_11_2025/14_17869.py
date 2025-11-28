from string import printable
def convert(num,sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2025
numx = convert(num, 25)
con = numx.count('0')
print(con)
#10