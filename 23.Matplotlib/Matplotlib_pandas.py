import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd


df = pd.read_csv('/Users/sotala/Desktop/AVSCODE/O.TEST/23.Matplotlib/data.csv')

type_counts = df['Type1'].value_counts(ascending=True)

plt.barh(type_counts.index, type_counts.values, color='darkblue')
plt.title('Type Counts')
plt.xlabel('Count')
plt.ylabel('Type')

plt.tight_layout() # To ensure everything fits without overlap

plt.show()