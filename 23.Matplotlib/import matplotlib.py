import matplotlib.pyplot as plt 
import numpy as np

year = np.array([2016, 2017, 2018, 2019, 2020])
y1 = np.array([20, 3, 15, 17, 2])
y2 = np.array([17, 23, 19, 13, 9])
y3 = np.array([25, 18, 23, 6, 19])

line_style = dict(marker='o',
                        ms=8,   
                        label='y1')

plt.title('Sample Line Plot', fontsize = 30, 
                            color = 'purple', 
                            loc = 'center', 
                            size = 'large',
                            font = 'Arial', 
                            weight = 'bold',
                            pad=20)

plt.xlabel('Year', fontsize=20, color='brown')
plt.ylabel('Values', fontsize=20, color='brown')


plt.plot(year, y1, **line_style, color='green')
plt.plot(year, y2, **line_style, color='blue')
plt.plot(year, y3, **line_style, color='red')

plt.tick_params(axis='x', labelsize=15, labelcolor='orange')

plt.xticks(year)


plt.show()



