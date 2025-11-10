from turtle import *
screensize(6000 * 6000)
m = 25
tracer(False)
rt(90)
pd()
for i in range(7):
    rt(45)
    fd(11 * m)
    rt(45)
up()
for x in range(-20, 30):
    for y in range(-20, 30):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()
#113