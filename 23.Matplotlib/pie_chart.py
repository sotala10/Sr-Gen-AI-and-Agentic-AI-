import matplotlib.pyplot as plt
import numpy as np 

#Pie chart - A pie chart is a circular statistical graphic, which is divided into slices to illustrate numerical proportion.

categories = np.array(['Freshman', 'Sophomore', 'Junior', 'Senior', 'Graduate'])
values = np.array([50, 40, 30, 20, 10])

plt.pie(values, labels = categories, 
                autopct='%1.1f%%', # show percentages
         colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink'], 
         explode=(0.1, 0, 0, 0, 0), # "explode" the 1st slice
         shadow=True)

plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Student Distribution by Year', fontsize=20, size = 'large', 
                        weight = 'bold')

plt.show()

