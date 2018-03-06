# sudo apt-get install python-matplotlib
# sudo apt-get install python-tk

import numpy as np
import matplotlib.pyplot as plt

# list of queries results
q_result = [3, 12, 5, 18, 45]

# list of queries names
q_name = ('query1', 'query2', 'query3', 'query4', 'query5')
y_pos = np.arange(len(q_name))

# create bars
plt.bar(y_pos, q_result)

# create names on the x-axis
plt.xticks(y_pos + .4, q_name, color='red')
plt.yticks(color='red')

# add title and name to the axes
plt.title("Queries compare Histogram")
plt.xlabel("Query name")
plt.ylabel("Query result")

plt.show()
