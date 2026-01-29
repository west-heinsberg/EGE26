from string import printable

alph = printable[:14]

max_val = 0
cnt = 0

for x in range(10, 14):
    for y in range(9, x):

        xi = alph[x]
        yi = alph[y]

        n1 = int(f'7{xi}37{yi}', 14)
        n2 = int(f'9{yi}63', x)
        n3 = int(f'15148', y)
        val = n1 + n2 - n3

        if val > max_val:
            max_val = val
            cnt = val // (x + y)

print(cnt)