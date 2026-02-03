def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            # d |= {i, num // i} #        объед-е мнж-в
            if i % 2 != 0: d |= {i}
            if num // i % 2 != 0: d |= {num // i}

    # ans = []
    # for i in d:
    #     if i % 2 != 0:
    #         ans += [i]

    # if len(ans) == 3:
    #     return sorted(ans)
    # # return False # так лучше не делать тк в одном случ-е ф-я возвр список в а другом логич. утверд. Проблема типов данных
    # return []

    if len(d) == 3:
        return sorted(d)
    return []


for n in range(18_782, 18_823):
    M = f(n)
    if M:
    # M := f(N) # моржов. оператор
        print(*M)