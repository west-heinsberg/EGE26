from string import printable as alph
for x in alph[:23]:
    num_1 = int(f'7{x}38596',23)
    num_2 = int(f'14{x}36',23)
    num_3 = int(f'61{x}7',23)
    num = num_1 + num_2 + num_3
    if num % 22 == 0:
        print(x, num // 22)
#47163321