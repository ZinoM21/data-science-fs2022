import pandas as pd
import seaborn as sns
df = sns.load_dataset('titanic')

# Task 1: Display the DataFrame

print(df)

# Task 2: Display the first 5 rows

print(df.head())

# Task 3: Display the last 5 rows

print(df.tail())

# Task 4: Display the number of rows and columns

print(df.shape)

# Task 5: Display the column names

print(df.columns)

# Task 6: List the row index

print(df.index)

# Task 7: Display the column types

print(df.dtypes)




