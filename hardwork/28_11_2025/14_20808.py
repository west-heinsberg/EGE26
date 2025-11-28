from string import printable
def convert(num,sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ansx =[]
ansc = []
for x in range(1,2031):
    num = 7**170 + 7**100 - x
    num7 = convert(num,7)
    con = num7.count('0')
    ansx.append(x)
    ansc.append(con)

print(ansx)
print(ansc)


