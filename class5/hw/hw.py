import turtle as t

t.color('red')
t.penup()
t.speed(0)
t.stamp()
for a in range(0, 8):
    t.home()
    t.right(45 * a)
    t.forward(80)
    t.stamp()

t.done()
