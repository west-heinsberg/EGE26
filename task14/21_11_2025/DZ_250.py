ans = []
for n in range(1, 41):
    b = bin(n)[2:]
    if b[-4:] == '1011':
        ans.append(n)
print(max(ans))
#27