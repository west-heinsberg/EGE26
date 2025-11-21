from string import printable as alph
for x in alph[:22]:
    num_1 = int(f'18{x}89957',22)
    num_2 = int(f'80{x}33',22)
    num_3 = int(f'521{x}6',22)
    num = num_1 + num_2 + num_3
    if num % 21 ==0:
        print(x, num // 21)
# 162947670