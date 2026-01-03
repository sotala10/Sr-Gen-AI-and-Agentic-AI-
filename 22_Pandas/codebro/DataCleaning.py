
import pandas as pd

# The process of cleaning and removing, incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data 
# within a dataset.
# 75% of work done with pandas is data cleaning.

df = pd.read_csv('/Users/sotala/Desktop/AVSCODE/O.TEST/Pandas/data.csv', index_col = "Name")
print(df)

print(df.to_string()) 

df_updated = df.drop(columns = ['Legendary'])
print("DataFrame after removing 'Legendary' column:")
print(df_updated.to_string())

# Handling missing values
# drop all the rows with missing values in 'Type2' column
df_with_missing_type2 = df.dropna(subset= ['Type2'])
print("DataFrame after removing rows with missing 'Type2' values:")
print(df_with_missing_type2.to_string())

# Fill missing values in 'Type2' column with 'Unknown'
df_filled_type2 = df.fillna({'Type2' : "None"})
print("DataFrame after filling missing 'Type2' values with 'None':")
print(df_filled_type2.to_string())  

# Fix inconsistent data
# Standardize 'Type1' column to have consistent capitalization
# convert type1 to upper case 

df['Type1'] = df['Type1'].replace({'Grass': 'GRASS', 'Fire': 'FIRE', 'Water': 'WATER'}
                                  )
print("DataFrame after standardizing 'Type1' values:")
print(df.to_string())

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()
print("DataFrame after removing duplicate rows:")
print(df_no_duplicates.to_string())

# Standardize column names text 
df['Name'] = df['Name'].str.lower()
print("DataFrame after standardizing 'Name' values to lowercase:")
print(df.to_string())

# convert data types
df['Legendary'] = df['Legendary'].astype(bool)
print("DataFrame after converting 'Legendary' column to boolean type:")
print(df.to_string())

