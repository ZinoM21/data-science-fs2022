import pandas as pd
import seaborn as sns
df = sns.load_dataset('titanic')

# Task 1: Write the data to a CSV file

df.to_csv('titanic.csv')

# Task 2: Read the CSV file to a new DataFrame

df2 = pd.read_csv('titanic.csv')

# Task 3: Write the data to an Excel file

df.to_excel('titanic.xlsx')

# Task 4: Read the Excel file to a new DataFrame

df3 = pd.read_excel('titanic.xlsx')

# Task 5: Write the data to a JSON file

df.to_json('titanic.json')

# Task 6: Read the JSON file to a new DataFrame

df4 = pd.read_json('titanic.json')

# Task 7: Make sure all data frames have the same shape

print(df.shape)