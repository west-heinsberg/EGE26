from string import printable
def convert(num,sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []
# max_r = 0
# ans_n = 0

for n in range(1, 100_000):
    r = convert(n,7)

    if r[-1] == '2':
        r = r.replace('3', '*')
        r = r.replace('1', '3')
        r = r.replace('*', '1')
        r = '21' + r
    else:
        r = r + '36'
        r = '1' + r[1:]

    r_val = int(r, 7)

    # if r_val < 744:
    #     if r_val > max_r:
    #         max_r = r_val
    #         ans_n = n
    #     elif r_val == max_r:
    #         if n < ans_n:
    #             ans_n = n

# print(ans_n)
    if r_val < 744:
        ans.append([r_val,n])
        ans = sorted(ans,key=lambda x:(-x[0],x[1]))
        print(ans[0])
#13