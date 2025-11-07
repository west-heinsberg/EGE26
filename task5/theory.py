# Системы счисления

# Двоичная система
N = 25 #ячейка памяти
# bin() - переводит десятичное число в двоичную систему.
# Принимает на вход int, возвращает str.
# [2:] - срез, убирающий первые два символа '0b'
print(bin(N)[2:]) #бинарная система
# f'' - форматируемая строка, которая позволяет вставлять в себя переменные
print(f'{N:b}')

# Восьмеричная СС
print(oct(N)[2:])
print(f'{N:o}')
# Шестнадцатеричная СС
print(hex(N)[2:])
print(f'{N:x}')

# Перевод в любую систему (2 <= sys <= 9)
def convert(num, sys):
    res = ''
    while num != 0:
        res = res + str(num % sys)
        # RES += str(num % sys)
        num = num // sys
        # num //= sys
    return res[::-1]

# print(convert(25,3))

# Перевод в любую систему (2 <= sys <= 36)
from string import printable # as alph - псевдоним (любой), потом исправить ниже

def convert2(num, sys):
    res = ''
    while num != 0:
        res += printable[num % sys]
        num = num // sys
        # num //= sys
    return res[::-1]

# Перевод в 10 СС
num_bin ='101'
num_tri = '121'
num_hex= 'fa8'

print(int(num_bin), 2)) #изначально из 10 в 10, => указ. сист. счисл.
print(int(num_bin), 3))
print(int(num_bin), 16))
