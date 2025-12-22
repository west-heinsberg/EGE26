from itertools import permutations

graph = 'AF AB AD DE BE EG GC CF FB'.split()
matrix = '37 367 125 56 34 247 126'.split()

print(*range(1, 8))

for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)

#66