def f(num):
    d = set() # множество чтобы отсеять все повтор. делители. ex. корень из 36 = 6, 6 * 6 надо исключить
    for i in range(2, int(num ** .5) + 1): # от 2 по усл!!
        if num % i == 0:
            # d.add(i)
            # d.add(num // i)
            d |= {i, num // i} # | - отвечает за обьед. множ-ва
            # нуен дел мн оканч на 8 и min

    for i in sorted(d):
        if i % 10 == 8 and i != 8:
            return i
    return 0


    # d_8 = []
    # for i in d:
    #     if i % 10 == 8 and i != 8:
    #         d_8 += [i] #
    #
    # if d_8:
    #     return min(d_8)
    # return 0

cnt = 0
for N in range(500_001, 10 ** 20):
    M = f(N)
    if M:
        print(N, M) # число, делитель
        cnt += 1 # нашли еще 1 число ""
        if cnt == 5:
            break
