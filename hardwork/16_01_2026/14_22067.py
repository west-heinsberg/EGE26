from string import printable
def convert(num,sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

x = convert(3 * 17**777 + 15*17**250 - 6*17**100 + 2, 17)
for i in printable[1:17:2]:
    x = x.replace(i,'')
print(len(set(x)))


# 2 способ
# chet = []
# while num:
#     if num % 17 % 2 == 0: # проверяем четную 17-ричн цифру
#         chet.append(num % 17)
#     num //= 17
# print((len(set(chet))))
# 4



