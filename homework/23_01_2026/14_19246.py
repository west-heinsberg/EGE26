from string import printable

for x in printable[:25]:
    n1 = int(f'11353{x}12',25)
    n2 = int(f'135{x}21',25)
    num = n1 + n2
    if num % 24 == 0:
        print(x, num // 24)
# 266249847