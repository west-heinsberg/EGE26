from string import printable as alph
for x in alph[:16]:
    num_1 = int(f'11{x}73',16)
    num_2 = int(f'94662{x}53{x}',16)
    num_3 = int(f'6{x}41',16)
    num_4 = int(f'31{x}77',16)
    num_5 = int(f'9{x}82{x}{x}181',16)
    num = num_1 + num_2 + num_3 + num_4 + num_5
    if num % 15 == 0:
        print(x, num // 15)
#5510300005, уточ 0 знач