x = 15 * 49 ** 237 + 37 *  343 ** 500 - 14 * 7 ** 35

cnt = 0

while x != 0:
    z = x % 49
    if z > 15:
        cnt += 1
    x //= 49
print(cnt)
# 220