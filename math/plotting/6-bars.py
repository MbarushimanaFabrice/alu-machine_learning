#!/usr/bin/env python3
"""Plot a stacked bar graph of fruit quantities per person."""
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

names = ['Farrah', 'Fred', 'Felicia']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
labels = ['apples', 'bananas', 'oranges', 'peaches']

bottom = np.zeros(3)
for row, color, label in zip(fruit, colors, labels):
    plt.bar(names, row, width=0.5, bottom=bottom, color=color, label=label)
    bottom += row

plt.ylabel('Quantity of Fruit')
plt.ylim(0, 80)
plt.yticks(range(0, 81, 10))
plt.title('Number of Fruit per Person')
plt.legend()
plt.show()
