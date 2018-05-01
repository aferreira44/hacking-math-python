from turtle import Turtle, exitonclick

tur = Turtle()
tur.speed(0)

def multi_cross():
  for i in range(2):
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
        tur.setpos(round(tur.xcor()+100), round(tur.ycor()-50))
        tur.pendown()

      tur.penup()
      tur.setpos(tur.xcor()-250, tur.ycor())
      tur.pendown()
    
    tur.penup()
    tur.setpos(100, -100)
    tur.rt(45)
    tur.setpos(tur.xcor()-50, tur.ycor()+150)
    tur.pendown()

multi_cross()

exitonclick()