import matplotlib.pyplot as plt

listX = [1, 2, 3, 4, 5, 6]
listY = [20, 30, 27, 21, 33, 40]

fig, ax = plt.subplots()
ax.plot(listX, listY)
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.set_title('Ya')

plt.show()