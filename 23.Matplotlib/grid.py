import matplotlib.pyplot as plt
import numpy as np

#grid() function adds grid lines to the plot

year = np.array([2016, 2017, 2018, 2019, 2020])
y1 = np.array([20, 3, 15, 17, 2])
y2 = np.array([17, 23, 19, 13, 9])


plt.plot(year, y1, marker='o', ms=8, label='y1')
plt.plot(year, y2, marker='o', ms=8, label='y2')

plt.xticks(year)

#plt.grid(True)
plt.grid(axis='y', color='gray', linestyle='--', linewidth=0.5)

plt.show()
