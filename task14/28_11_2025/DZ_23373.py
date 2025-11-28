num = 2 * 2401**525 + 3*343**524 - 4*49**523 + 5*49**522 - 6*7**521 - 35
count = 0
while num > 0:
    if num % 49 <= 9:
        count += 1
    num = num // 49
print(count)
#не выполняется