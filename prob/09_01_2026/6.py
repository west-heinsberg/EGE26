from turtle import *
tracer(False)
screensize(3000,3000)
m = 20

pd()
for govno in 0,2:
    fd(14 * m)
    lt(270)
    bk(12* m)
    rt(90)
up()
fd(9* m)
rt(90)
bk(7* m)
lt(90)
pd()
for kek in 0,2:
    fd(13* m)
    rt(90)
    fd(6* m)
    rt(90)

up()
update()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x * m, y * m)
        dot(3,'red')
update()
done()