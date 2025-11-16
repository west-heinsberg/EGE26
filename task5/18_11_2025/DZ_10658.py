def convert(sys, num):
    res = ''
    if num == 0:
        return '0'
    while num != 0:
        res = res + str(num % sys)
        num = num // sys
    return res[::-1]


ans = []

for n in range(11, 100_000):
    r = convert(3, n)
    chet = r.count('0') + r.count('2')
    #нечет 1
    nechet = r.count('1')

    if chet > nechet:
        r_res = '22' + r
    else:
        r_res = '11' + r

    R = int(r_res, 3)

    if R > 100:
        ans.append(R)

print(min(ans))
#120