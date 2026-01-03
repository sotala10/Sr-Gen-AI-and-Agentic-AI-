#Dataframe Operations in Pandas
#Dataframe isa tabular data structure with labeled axes (rows and columns) (2 Diemsnions, Similar to excel spreadsheet or SQL table))

import pandas as pd

data = {'Name': ['Spongebob', 'Patrick', 'Squidward'],
        'Age': [30, 35, 50]
}

#creating a dataframe from dictionary
df = pd.DataFrame(data)
print(df)

# Accessing rows by label
df = pd.DataFrame(data, index = ['Employee1', 'Employee2', 'Employee3'])

print(df.loc['Employee1'])  # Access by label

# Accessing rows by position
print(df.iloc[2])  # Access by position

# Conditional filtering
print(df[df['Age'] > 30])  # Employees aged 30 or older    

# Adding a new column

df["job"] = ["cook", "N/A", "Cashier"]
print(df)

# Add a new row
new_row = pd.DataFrame([{'Name': 'Sandy', 'Age': 28, 'job': 'Engineer'}], index = ['Employee4'])

df = pd.concat([df, new_row])
print(df)

# Adding multiple new rows

new_rows = pd.DataFrame([{'Name': 'Eugene', 'Age': 60, 'job': 'Manager'},
                        {'Name': 'Vemana', 'Age': 40, 'job': 'Software Engineer'}], index = ['Employee5', 'Employee6'])

df = pd.concat([df, new_rows])
print(df)

