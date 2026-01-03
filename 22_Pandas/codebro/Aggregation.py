
import pandas as pd

# reduce a set of values down to a single value used to summarize and analyze daya, often used in conjunction 
# with groupby method

df = pd.read_csv('/Users/sotala/Desktop/AVSCODE/O.TEST/Pandas/data.csv', index_col = "Name")
print(df)

print(df.to_string()) 

# find the mean height of all pokemon

mean_height = df['Height'].mean()
print("Mean Height of all Pokémon:", mean_height)

# Aggreate functions on entire DataFrame

print(df.mean(numeric_only = True))  # Mean of all numeric columns
print(df.sum(numeric_only = True))  # Sum of all numeric columns
print(df.min(numeric_only = True))  # Minimum of all numeric columns
print(df.max(numeric_only = True))  # Maximum of all numeric columns
print(df.count())  # Count of all numeric columns


# Aggregate functions on Single column

print("Mean of Height: ", df['Height'].mean())  # Mean of Height column
print("Sum of Height: ", df['Height'].sum())  # Sum of Height column
print("Minimum of Height: ", df['Height'].min())  # Minimum of Height column
print("Maximum of Height: ", df['Height'].max())  # Maximum of Height column
print("Count of Height: ", df['Height'].count())  # Count of Height column


# Aggregate functions on Grouped Data

#Put all the  types of pokemon together (Type 1)

group = df.groupby('Type1')
print(group["Height"].mean())  # Mean Height for each Type1
print(group["Height"].sum())  # Sum Height for each Type1
print(group["Height"].min())  # Minimum Height for each Type1

print(group["Height"].max())  # Maximum Height for each Type1
print(group["Height"].count())  # Count of Height for each Type1    


