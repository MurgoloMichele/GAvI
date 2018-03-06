#import main_parser*

#query_results = funzione_recupero_query

# libraries
import numpy as np
import matplotlib.pyplot as plt

# Choose the height of the bars
height = [3, 12, 5, 18, 45]

# Choose the names of the bars
bars = ('group1', 'group2', 'group3', 'group4', 'group5')
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height)

# Create names on the x-axis
plt.xticks(y_pos, bars, color='orange')
plt.yticks(color='orange')

# Show graphic
plt.show()
