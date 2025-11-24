from string import printable as alph
for z in range(16,36):
    num_1 = int('17496',z)
    num_2 = int('91F83',z)
    num_3 = int('D9543',z)
    num = num_1 + num_2 + num_3
    if num % 12 == 0:
        print(num // 12)