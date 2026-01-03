import pandas as pd


data = [100, 102, 104, 106, 200, 202]


series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f'])
print(series)

print(series.loc['b'])  # Access by label

print(series.iloc[2])  # Access by position

print(series[series >= 200])  # Conditional filtering

#disctionary to series

calories = {'Day 1': 1750, 'Day 2': 2100, 'Day 3': 1700}

series = pd.Series(calories)
print(series)

print(series.loc['Day 2'])  # Access by label

series.loc['Day 3'] += 500
print(series)

# Days where calories consumed were at least 2000
print(series[series >= 2000])  # Conditional filtering

# return days where calories consumed were less than 1800
print(series[series < 1800])  # Conditional filtering


