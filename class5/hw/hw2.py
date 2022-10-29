import turtle as t
import time as ti

t.tracer(1, 0)
t.left(90)
for a in range(1, 61):
    t.right(6 * a)
    t.forward(80)
    t.home()
    t.left(90)
    ti.sleep(1)
    t.clear()