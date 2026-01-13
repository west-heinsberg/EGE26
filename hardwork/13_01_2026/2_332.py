# print('------')
# for x in  0,1:
#     for y in  0, 1:
#         for z in  0, 1:
#             for w in  0, 1:
#                 f = (x and y or (not z))
#                 if f == 1:
#                     print(x,y,z,w)

from itertools import *
def f(x,y,z,w):
    return (x or y and not z) and not w

table= [
    (1,0,0,0),
    (0,0,1,0),
    (0,1,0,1),
]
for p in permutations('xyzw'):
    if [f(**dict(zip(p,t))) for  t in table] == [1,1,0]:
        print(*p, sep = '')