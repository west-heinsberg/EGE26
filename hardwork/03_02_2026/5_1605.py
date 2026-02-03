def convert(num,sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []




for n in range(1,100_000):
    r = convert(n, 2 + n)
    r += str(r.count('1') % 2)
    r += str(r.count('1') % 2)
    r = int(r, 2)
    if n < 61:
        ans.append(n)

print(max(ans))
