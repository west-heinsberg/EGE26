from string import printable as alph


def convert(num, sys):
    res = ''
    while num:
        res = res + alph[num%sys]
        num //= sys
    return res[::-1]

num_10 = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
num_27 = convert(num_10, 27)

cnt = 0
for i in num_27:
    if int(i,27) > 9:
        cnt += 1
print(cnt)

############################################ 2 способ

cnt2 = 0
for i in alph[10:27]:
    cnt2 += num_27.count(i)
print(cnt2)

################################################

cnt3 = 0
for i in num_27:
    if i in alph[10:27]:
        cnt3 += 1
print(cnt)
