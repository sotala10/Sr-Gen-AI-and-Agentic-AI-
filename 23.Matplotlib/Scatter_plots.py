import matplotlib.pyplot as plt
import numpy as np 

# Scatter graph - shows the relationship between two variables
#    Helps identify correlations, trends, and outliers in data sets.
#    Example Study hours vs exam scores.


z1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y1 = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

z2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y2 = np.array([50, 65, 33, 44, 22, 55, 10, 99, 66, 78])

plt.scatter(z1, y1, color='r', 
            marker='o', 
            s = 50,  # size of markers
            edgecolor='black',
            alpha=0.9, 
            label= 'CLASS A')  # alpha for transparency

plt.scatter(z2, y2, color='b', 
            marker='o', 
            s = 50,  # size of markers
            edgecolor='black',
            alpha=0.9, 
            label = 'CLASS B')  # alpha for transparency

plt.title('Study Hours vs Exam Scores', fontsize=16, color='black')

plt.xlabel('Study Hours', fontsize=14, color='Orange', weight='bold')
plt.ylabel('Exam Scores', fontsize=14, color='Orange', weight='bold')

plt.legend()  # Show the legend for the classes 
plt.show()
           
        

                        
                        
