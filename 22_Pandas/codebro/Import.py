#Importing csv and Json files using pandas

import pandas as pd

df = pd.read_csv('/Users/sotala/Desktop/AVSCODE/O.TEST/Pandas/data.csv', index_col = "Name")
print(df)

print(df.to_string())  # Display the entire DataFrame

#Selection Techniques from teh data frame 

#selection by column
#print(df["Name"])  # Accessing 'Name' column

#print(df['Height'])  # Accessing 'Height' column

#print(df['Weight']) # Accessing 'Weight' column

#print(df[['Name', 'Height', 'Weight']].to_string() )  # Accessing multiple columns


#selection by row

print(df.loc['Venonat'])  # Accessing row with index name

print(df[df['Weight'] > 15])  # Rows where 'Weight' is greater than 15

#access by interger location
print(df.iloc[0:11])  # Accessing first 11 rows

#access by interger location
print(df.iloc[0:11:4, 0:3])  # Accessing first 11 rows by step 4 and first 3 columns

pokemon = input ("Enter the pokemon name: ")

try:
    print(df.loc[pokemon])  # Accessing row with index name
except KeyError:
    print("Pokemon not found in the DataFrame.")
    
    

    
