import matplotlib.pyplot as plt
y = [2, 3, 5, 7, 11]
x = [value * 2 for value in y]
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Sample Graph')
plt.show()