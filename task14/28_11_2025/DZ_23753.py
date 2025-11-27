from string import printable
for x in printable[:29]:
    num_1 = int(f'923{x}874',29)
    num_2 = int(f'524{x}6152',29)
    num = num_1 + num_2
    if num % 28 == 0:
        print(x, num // 28)
#3319197720