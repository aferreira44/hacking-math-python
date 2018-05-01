from turtle import Turtle, exitonclick

tur = Turtle()
tur.speed("fastest")

def pyramid(size, step):
  tur.rt(90)
  for i in range(int(size/step)):
    tur.fd(size)
    tur.lt(90)
    size -= step

pyramid(300, 2)

exitonclick()