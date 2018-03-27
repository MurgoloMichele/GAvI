# see https://matplotlib.org/users/pyplot_tutorial.html
import matplotlib.pyplot as plt

class GraphXY:

    # given the data on the x axis, the values on the y axis are auto determined
    def __init__(self, recall, precision):
        self.x = recall
        self.y = precision

    def plot(self):
        # plt.plot(x, y, color)
        plt.plot(self.x, self.y, color='green')

        # add title and name to the axes
        plt.title('Precision-Recall')
        plt.xlabel('Recall')
        plt.ylabel('Precision')

        plt.show()
