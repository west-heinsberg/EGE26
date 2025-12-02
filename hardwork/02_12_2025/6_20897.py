from turtle import *
screensize(3000,3000)
m = 20
# * m
pendown()
tracer(False)

for i in range(9):
    fd(27* m)
    rt(90)
    fd(30* m)
    rt(90)
pu()
fd(3* m)
rt(90)
fd(6* m)
lt(90)
pd()
for i in range(9):
    fd(77* m)
    rt(90)
    fd(66* m)
    rt(90)

pu()

for x in range(-30,60):
    for y in range(-30,60):
        goto(x* m,y * m)
        dot(7, 'white')
update()
done()

