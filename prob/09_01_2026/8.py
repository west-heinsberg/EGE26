from itertools import product

cnt = 0

for val in product([val for val in range(25)],repeat=4):
    if val[0] != 0:
        if sum(z % 2 != 0 for z in val) == 1 and sum(1 for z in val if z <= 5) <= 2:
            cnt += 1
print(cnt)








#     if val[0] != '0':
#         if val.count('1') == 1  or val.count('3') ==1 or val.count('5')==1 or val.count('7')==1 or val.count('9') == 1:
#             for i in val:
#                 if int(val[i],25) > 5:
#                     cnt += 1
#                     print(val)
# print(cnt)
