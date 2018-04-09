import numpy as np
import matplotlib.pyplot as plt


class Histogram:

    def __init__(self, q_results):
        # list of queries results
        self.result = q_results

    def plot(self):
        # list of queries names
        q_name = ('query1', 'query2', 'query3', 'query4', 'query5')
        y_pos = np.arange(len(q_name))

        # create bars
        plt.bar(y_pos, self.result)

        # create names on the x-axis
        plt.xticks(y_pos + .4, q_name, color='red')
        plt.yticks(color='red')

        # add title and name to the axes
        plt.title("Queries compare Histogram")
        plt.xlabel("Query name")
        plt.ylabel("Query result")

        plt.show()