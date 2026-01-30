def f2(num):
    d = []
    if num % i == 0:
        d.append(i)
    d.append(num)

def f3(num):
    d = []
    for i in range(1, int(num ** .5) + 1):
        if num % i == 0:
            d.append(i)
            d.append(num // i)