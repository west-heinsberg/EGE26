from itertools import combinations
def f(x):
    b = 36 <= x <= 75
    c = 60 <= x <= 110
    a = A1 <= x <= A2
    return ((not a) <= (b == c))

line_A = [36,60,75,110]
line_x = [37,45,75]

ans = []
for A1, A2 in combinations(line_A,2):
    if all(f(x) for x in line_x):
        ans.append(A2 - A1)
print(max(ans))

# 74
