from timeit import repeat

x = int(input(''))
for i in range(x):
    a = x - i - 1
    b = i * 2 + 1
    print(' ' * a + '*' * b)

for i in range(x):
    print(' ' * (x - 1) + '*' * 1)
