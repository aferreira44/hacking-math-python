from turtle import Turtle, exitonclick

tur = Turtle()
tur.speed("normal")

def multi_cross():
  for i in range(2):
    for i in range(2):
      for i in range(4):
        tur.fd(50)
        tur.lt(90)
        tur.fd(50)
        tur.rt(90)
        tur.fd(50)
        tur.rt(90)

      tur.penup()
      tur.setpos(tur.xcor()+100, tur.ycor()-50)
      tur.pendown()

    tur.penup()
    tur.setpos(tur.xcor()-250, tur.ycor())
    tur.pendown()

  tur.penup()
  tur.setpos(100, -100)

multi_cross()

exitonclick()