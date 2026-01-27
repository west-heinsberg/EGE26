from fnmatch import fnmatch

for n in range(12347 - 12347 % 141, 10**8 + 1, 141): #тк ищем числа к-ые дел на 141 по усл но 10**8 слишком большое и будет долго счтитаь
    if fnmatch(str(n), '1234*7'): # and n % 141 == 0: #стр тк фнматч раб со строками
        print(n,n // 141)

# второй способ если фнматч работает 100000 лет ""
#################################################

from itertools import product
from string import printable

# 100000000
# 12349997 - нельзя подст

ans = []

for l in range(0,4):
    for Z in product(printable[:10], repeat=l):
        num = int('1234' + ''.join(Z) + '7')
        if num % 141 == 0 and num <= 10**8:
            ans.append([num, num // 14])

for i in sorted(ans):
    print(*i)

