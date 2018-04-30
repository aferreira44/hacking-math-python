from turtle import Turtle, exitonclick

tur = Turtle()
tur.speed("fastest")

def circle():
  for i in range(360):
    tur.fd(1)
    tur.rt(1)

def quartercircle():
  for i in range(90):
    tur.fd(1)
    tur.rt(1)

def petal():
  '''This draws a petal.'''
  for i in range(2):
    quartercircle()
    tur.rt(90)

def flowerhead():
  '''This draws a flower head.'''
  for i in range(12):
    petal()
    tur.rt(30)

def flower():
  '''This draws a flower.'''
  tur.color('green')
  tur.pensize(3)
  tur.setpos(0, -200)
  tur.setheading(90)
  tur.fd(100)
  petal()
  tur.fd(150)
  tur.color('pink')
  flowerhead()

flower()

exitonclick()