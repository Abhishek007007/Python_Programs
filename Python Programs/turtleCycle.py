import turtle as t

def moveCycle(bike):
    temp = bike.pos()
    bike.pensize(5)
    bike.setheading(80)
    bike.forward(70)
    bike.setheading(0)
    bike.forward(5)
    bike.setheading(180)
    bike.forward(10)
    bike.setheading(0)
    bike.forward(5)
    bike.setheading(260)
    bike.forward(70)
    bike.setheading(0)
    bike.fillcolor('black')
    bike.begin_fill()
    bike.circle(25)
    bike.end_fill()
    bike.setheading(90)
    bike.forward(20)
    bike.setheading(0)
    bike.forward(100)
    bike.setheading(270)
    bike.forward(20)
    bike.setheading(0)
    bike.begin_fill()
    bike.circle(20)
    bike.end_fill()
    bike.setheading(110)
    bike.forward(60)
    bike.setheading(180)
    bike.forward(70)
    bike.setheading(0)
    bike.forward(70)
    bike.setheading(110)
    bike.forward(20)
    bike.setheading(170)
    bike.forward(10)
    bike.setheading(350)
    bike.forward(20)
    bike.setheading(0)
    bike.penup()
    bike.setpos(temp)
    bike.pendown()

if __name__ == "__main__":
    scr = t.Screen()
    scr.setup(650, 650)
    scr.bgcolor('light green')
    scr.tracer(0)

    bike = t.Turtle()
    bike.speed(0)
    bike.width(2)
    bike.hideturtle()
    bike.penup()
    bike.goto(-350, 0)
    bike.pendown()
    while True:
        bike.clear()
        moveCycle(bike)
        scr.update()
        bike.forward(.6)

t.done()