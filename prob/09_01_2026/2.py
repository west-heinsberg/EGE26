for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = (z <= y) or ((w <= x) <= y)
                if f == 0:
                    print(y,w,x,z)
#ywxz