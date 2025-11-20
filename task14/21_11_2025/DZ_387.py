def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

z = 51 * 7**12 - 7**3 - 22
z7 = convert(z, 7)
sum7 = sum(map(int,z7))
print(sum7)
#70