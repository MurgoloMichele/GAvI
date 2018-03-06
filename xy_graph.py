# see https://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt

# given the data on the x axis, the values on the y axis are auto determined

queries = [1, 2, 3, 4, 5, 6]
model1 = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
model2 = [49.48, 69.783, 110.4, 127.1, 130.1, 201.23]

# plt.plot(x, y, color)
plt.plot(queries, model1, color='green')
plt.plot(queries, model2, color='orange')

# add title and name to the axes
plt.title('Model compare')
plt.xlabel('Queries')
plt.ylabel('Model')

plt.show()
