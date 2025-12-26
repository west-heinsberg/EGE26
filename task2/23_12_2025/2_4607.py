print('X Y Z W')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x <= z) <= y) or not w
                if f == 0:
                    print(z,x,y,w)