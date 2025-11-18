def convert(num, sys):
    res = ''
    while num != 0:
        res = res + str(num % sys)
        # RES += str(num % sys)
        num = num // sys
        # num //= sys
    return res[::-1]

min_r = 10 ** 100
ans_n = 0
res = []
res_0 = []

for n in range(1,100_000):
    r_3 = convert(3,n)
    if n % 2 == 0:
        r = r + r[2:]
    else:
        r = r + convert((sum(map(int,r)), 3))
    r = int(r,3)
    ans.append([r,n]) # сохран все пары

print(min(ans)) # берёт минимальный по перв элементу
    #res.append(r)
    #res_0.append(n)
#    if r < min_r:
 #       min_r = r
  #      ans_n = n
#print
#print(res_0[res.index(min(res))])
