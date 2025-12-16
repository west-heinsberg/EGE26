from itertools import product

list1 = []
list2 = []

for val in product('КОНЕЦ',repeat=5):
    val = ''.join(val)
    list1.append(val)

for val in product('ДРАКОН',repeat=5):
    val = ''.join(val)
    list2.append(val)

list3 = []
for val in product('КОН',repeat=5):
    val = ''.join(val)
    list3.append(val)

print(len(list1) + len(list2) - 2*len(list3))
#10415

################
# 2 способ
#после второго листа
# #cnt = 0
# for i in list1:
#     if i not in