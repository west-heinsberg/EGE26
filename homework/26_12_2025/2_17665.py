for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (z <= (not(y <= x))) or w
                if f == 0: print(z,y,x,w)
#zyxw
