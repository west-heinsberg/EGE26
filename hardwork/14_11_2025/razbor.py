def transform(let):
    return int(let, 36)
num = '1653a' # -> map(transform, '1653a') -> 1 6 5 3 10 тк мэп передаёт

print(sum(map(transform, num))) #вместо деф, имя пишем лямбда чтобы не писать весь деф
# в случае деф с ретурн
# задача звук
# v = nkit
# k - каналы n('этта') - дискритиз

ans = []
for n in range(1, 100_000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + r[:3]
    else:
        r = '1' + r + '01'
        r = int(r, 2)
    if r > 600:
        ans.append(r)
print(min(ans)) # всегда используем
#ластовая
ans = []
for N in range(1, 100_000):
    R = convert(N, sys:4)
    if N % 4 == 0:
        R = '2' + R + '03'
    else:
    R += convert(N % 4 * 5, sys:4)
    if int(R, 4) < 567:
        ans.append(N)
print(max(ans))

num = '102321'
new_num =
for i in num:
    if i == '1':
        new_num += '3'
    elif i == '3':
        new_num += '1' else:
    new_num += i print(num)