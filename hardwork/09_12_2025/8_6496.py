from itertools import product

cnt = 0
cnt2= 0
cnt3 = 0
alph = sorted('БЕРСК')

for val in product(alph,repeat=5):
    val = ''.join(val)
    cnt += 1
for val in product(alph,repeat=6):
    val = ''.join(val)
    cnt2 += 1
for val in product(alph, repeat=7):
    val = ''.join(val)
    cnt3 += 1

print(cnt + cnt2 + cnt3)

##############################################
# 2 способ через for i
# for i in range(5,8):
# далее один фор вал