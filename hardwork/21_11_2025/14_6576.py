from string import printable
def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]
z = 283**382 + 9**15 + 2**3
z14 = convert(z,14)
conB = z14.count('11')
conC = z14.count('12')
print(conB - conC)
###################################################
#правильное ниже
cnt_b = 0
cnt_c = 0
a = 0
while z:
    if z % 14 == 11:
        cnt_b += 1
    if z % 14 == 12:
        cnt_c += 1
    z //= 14

print(abs(cnt_b - cnt_c))