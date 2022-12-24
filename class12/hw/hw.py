import turtle
import random as r


def tree_leaves(x, y):
    R = float(r.randint(0, 255)) / 255
    G = float(r.randint(0, 255)) / 255
    B = float(r.randint(0, 255)) / 255
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    # turtle.color('green')
    turtle.color(R, G, B)
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()


def tree_trunk(x, y):
    # R = float(r.randint(0, 255)) / 255
    # G = float(r.randint(0, 255)) / 255
    # B = float(r.randint(0, 255)) / 255
    turtle.penup()
    turtle.goto(x + 12.5, y)
    turtle.pendown()
    turtle.color('brown')
    # turtle.color(R, G, B)
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(25)
    turtle.end_fill()


turtle.speed(0)

for i in range(100):
    x = r.randint(-500, 300)
    y = r.randint(-200, 200)
    tree_leaves(x, y + 0)
    tree_leaves(x, y + 20)
    tree_leaves(x, y + 40)
    tree_trunk(x, y + 0)

# tree_leaves(0, 0)
# tree_leaves(0, 20)
# tree_leaves(0, 40)
# tree_trunk(0, 0)

turtle.done()