from turtle import *

speed('fastest')
pencolor('blue')
side=5

for i in range(side):
    pensize(1)
    fd(100)
    for i in range(side):
        pensize(2)
        fd(50)
        fillcolor('green')
        begin_fill()

        for i in range(side):
            pensize(3)
            fd(25)
            dot(10)
            lt(60)
        lt(60)
    lt(60)
    end_fill()
hideturtle()
mainloop()