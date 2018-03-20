# see https://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt

class GraphXY:

    # given the data on the x axis, the values on the y axis are auto determined
    def __init__(self, queries, m1, m2):
        self.queries = [1, 2, 3, 4, 5, 6] #queries
        self.model1 = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6] #m1
        self.model2 = [49.48, 69.783, 110.4, 127.1, 130.1, 201.23] #m2

    def plot(self):
        # plt.plot(x, y, color)
        plt.plot(self.queries, self.model1, color='green')
        plt.plot(self.queries, self.model2, color='orange')

        # add title and name to the axes
        plt.title('Model compare')
        plt.xlabel('Queries')
        plt.ylabel('Model')

        plt.show()
