from turtle import *

def triangle():
  for i in range(3):
    fd(100)
    rt(120)

def square(length = 100):
  for i in range(4):
    fd(length)
    rt(90)

def squareThing():
  color('green')
  for i in range(20):
      square()
      rt(10)

def octagon():
  for i in range(8):
    fd(100)
    rt(45)

def polygon(sides, length = 100):
  for i in range(sides):
    fd(100)
    rt(360/sides)

def circle():
  for i in range(360):
    fd(1)
    rt(1)

def spiral(times = 30):
  '''draws a spiral of squares.'''
  color('blue')
  length = 10
  for i in range(times):
    square(length)
    rt(5)
    length = length + 5

polygon(10)

exitonclick()