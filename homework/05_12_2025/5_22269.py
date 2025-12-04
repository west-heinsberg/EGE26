def convert(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

res = []

for n in range(1, 10000):
    r_5 = convert(n, 5)

    if r_5[-1] == '0':
        r_5 = r_5.replace('1', 'x')
        r_5 = r_5.replace('4', '1')
        r_5 = r_5.replace('x', '4')

        r_5 = '33' + r_5
    else:
        r_5 = r_5 + '42'
        r_5 = '3' + r_5[1:]
    r_v = int(r_5, 5)

    if r_v < 1922:
        res.append((r_v, n))

print(res)
#(497, 9) => 9