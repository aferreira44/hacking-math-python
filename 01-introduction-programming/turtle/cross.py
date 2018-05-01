from turtle import Turtle, exitonclick

tur = Turtle()
tur.speed("fast")

def cross():
  for i in range(4):
    tur.fd(100)
    tur.lt(90)
    tur.fd(100)
    tur.rt(90)
    tur.fd(100)
    tur.rt(90)

cross()

exitonclick()