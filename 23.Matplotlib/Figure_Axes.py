import matplotlib.pyplot as plt
import numpy as np

#Figure = The entire canvas or window where the plot is drawn
#Ax = A single plot or graph within the figure
# A figure can contain multiple axes (subplots)

figures, axes = plt.subplots(2, 2)

axes[0, 0].set_title('Plot1')
axes[0, 1].set_title('Plot2')
axes[1, 0].set_title('Plot3')
axes[1, 1].set_title('Plot4')

axes[0, 0].plot([1, 2, 3], [4, 5, 6], color='r')
axes[0, 1].plot([22, 33, 44], [22, 33, 51], color='g')
axes[1, 0].plot([5, 6, 7], [8, 9, 3], color='b')
axes[1, 1].plot([11, 22, 33], [44, 55, 59], color='y')


plt.show()


