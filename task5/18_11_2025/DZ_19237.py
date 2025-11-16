def convert(sys, num):
    res = ''
    if num == 0:
        return '0'
    while num != 0:
        res = res + str(num % sys)
        num = num // sys
    return res[::-1]

ans = []
for n in range(1, 10000):
    r_n = convert(3, n)

    if n % 3 == 0:
        r = r_n + r_n[-2:]
    else:
        sumd = sum(map(int, r_n))
        r_sumd_str = convert(3, sumd)
        r = r_n + r_sumd_str

    R = int(r, 3)

    if R > 220 and R % 2 == 0:
        ans.append(R)

if ans:
    print(min(ans))
#222