import turtle as t
import random as r


def tree_leaves(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.color('green')
    t.begin_fill()
    t.forward(130)
    t.left(150)
    t.forward(150)
    t.left(60)
    t.forward(150)
    t.end_fill()
    t.left(180)
    t.penup
    t.forward(150)
    t.right(30)
    t.forward(100)
    t.left
    t.end_fill()


def tree(x, y):
    t.penup()
    t.goto(x - 20, y + 5)
    t.color('brown')
    t.begin_fill()
    t.setheading(0)
    t.right(90)
    t.forward(120)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.end_fill()

    x = int(input('x'))
    y = int(input('y'))
    tree_leaves(x, y)
    tree(x, y)


t.done()