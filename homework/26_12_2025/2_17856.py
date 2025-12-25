for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = ((w <= y) <= x) or not z
                if f == 0: print(z,y,w,x)
#zywx
