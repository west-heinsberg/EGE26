from string import printable

for x in printable[1:8]: # начинаем не с 0-вой сис-мы
    n1 = int(f'{x}1{x}',16)
    n2 = int(f'{x}3{x}3',8)
    num = n1 + n2
    if num % 2 == 0:
        print(num,x)
    # for i in range(1,30):
    #   подбир степень
# 2 способ
from math import log2