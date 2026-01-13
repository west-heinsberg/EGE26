from itertools import product
from string import printable

c3 = 0
c5 = 0

for val in product(printable[:16], repeat=3):
    if val[0] > val[1] > val[2] and val[0] != val[1] != val[2] != val[0]:
        c3 += 1

for val in product(printable[:16], repeat=5):
    if val[0] > val[1] > val[2] > val[3] > val[4] and len(set(val)) == 5:
        c5 += 1

govn = c3 + c5
print(govn)
#4928