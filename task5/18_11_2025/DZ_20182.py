def convert(sys, num):
    res = ''
    if num == 0:
        return '0'
    while num != 0:
        res = res + str(num % sys)
        num = num // sys
    return res[::-1]


ans = []

for n in range(1, 100_000):
    r = convert(3, n)

    sumd = sum(map(int, r))

    if sumd % 2 == 0:
        r = r + '0'
        r_result = '12' + r[2:]
    else:
        r = r + '2'
        r_result = '10' + r[2:]

    R = int(r_result, 3)

    if R > 105:
        ans.append(n)

print(min(ans))
#28