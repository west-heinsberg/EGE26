from itertools import permutations

graph = 'EH HG GC CF FA AE ED HB GB FD DB'.split()
matrix = '367 568 18 58 247 127 56 234'.split()

print(*range(1, 9))
for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
# 21