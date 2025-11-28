from string import printable
def convert(num,sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

ans = []
# ans_r = []
# ans_n = []

for n in range(1,100_000):
    r = convert(n,4)
    if sum(map(int,  r)) % 3 == 0:
        r = r.replace('0', '*').replace('2', '0').replace('*', '2')
        r = '32' + r
    else:
        r += '33'
        r = r[0] + '10' + r[3:]
    r10 = int(r, 4)
    if r10 > 320:
    #if r == 335:
        ans.append(r10)
    # и меняем  на n

print(min(ans))
    # if r10 > 320:
        # ans_r.append(r10)
        # ans_n.append(n)

# min_r = min(ans_r)
# ans_max_n = []
# for i in range(len(ans_r)): #range под длине (10) -> 0 1 2 3 4 5 6 7 8 9
#     if ans_r[i] == min_r:
#         ans_max_n.append(ans_n[i]) #print(ans_n[i])
#
# print(max(ans_max_n))

#неуд // решено, разобрано
