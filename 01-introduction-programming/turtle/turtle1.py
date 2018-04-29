from turtle import *

def triangle():
  for i in range(3):
    fd(100)
    rt(120)

def square():
  for i in range(4):
    fd(100)
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

def circle():
  for i in range(360):
    fd(1)
    rt(1)

exitonclick()