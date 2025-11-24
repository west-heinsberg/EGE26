from string import printable as alph
for x in alph[:27]:
    num_1 = int(f'8{x}38{x}68',27)
    num_2 = int(f'37{x}3163',27)
    num = num_1 + num_2
    if num % 26 == 0:
        print(x, num // 26)
#176999110