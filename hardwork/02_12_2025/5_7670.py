ans_n = []
ans_r = []
for n in range(151,100_000):
    r = f'{n:x}'[2:]
    r = r.replace('a','1')
    z = r.count('0') + r.count('2') + r.count('4') + r.count('6') + r.count('8') + r.count('a') + r.count('c') + r.count('e')
    #for i in r:
    # if int(i,16) % 2 == 0:
    #     z += 1
    if z > 2:
        r = r + 'b'
    else:
        r = 'f' + r
    r = int(r,16)
    if r > 3500:
        ans_n.append([r,n])
print(min(ans_n))