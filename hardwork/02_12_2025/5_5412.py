ans = []
# k = 0
for n in range(1,10000):
    r = f'{n:x}'
    if r.count('b') % 2 == 0:
        r = '1' + r
    else:
        r = r + '1'
    r = int(r,16)
    # if r // 100 == 0 and r % 100 > 9:
    #     k += 1
    # через сравнение
    # if 10 <= r <= 99:
    # if len(str(r)) == 2:
    ans.append(r)
print(ans)
#14