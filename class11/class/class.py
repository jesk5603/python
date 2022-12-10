# def hellow(name):
#     print(f'hellow{name}')
# hellow(input('請輸入名稱:'))

# def my_min(a, b):
#     if a > b:
#         return a
#     else:
#         return b
# print(my_min(10, 5))

import random as r

# q = r.randint(1, 6)


def a():
    d = {}
    s = int(input('請輸入擲骰子次數'))
    for i in range(s):
        q = r.randint(1, 6)
        d[i + 1] = q
    return d


print(a())
