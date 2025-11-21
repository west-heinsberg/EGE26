from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

z = 729**8 - 3**18 + 85
z9 = convert(z,9)
print(z9.count('0'))