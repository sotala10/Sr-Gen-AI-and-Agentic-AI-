import matplotlib.pyplot as plt 
import numpy as np

# Bar chart compares categories of data by reprsenting each category with a bar whose height corresponds to the value of that category.

categories = np.array(['Greens', 'Fruits', 'Dairy', 'Meat', 'Beverages'])

values = np.array([20, 3, 15, 17, 2])
bar_colors = ['green', 'orange', 'blue', 'red', 'purple']

plt.bar(categories, values, color=bar_colors)
plt.xlabel('FOOD ITEMS', fontsize=15, color='brown')

plt.title('VEGETABLES', fontsize = 30, color = 'purple', loc = 'center', size = 'large',
                            font = 'Arial', weight = 'bold')


plt.show()


