import seaborn as sns
df = sns.load_dataset('titanic')

# Task 1: Display the 'fare' column

print(df['fare'])

# Task 2: Display the 'fare' and 'age' columns

print(df[['fare', 'age']])

# Task 3: Display the passenger with id 3

print(df.loc[3])

# Task 4: Display the passengers having ids 3, 5 and 8

print(df.loc[[3, 5, 8]])

# Task 5: Display the the 'fare' and 'age' columns for passengers with ids 3, 5 and 8

print(df.loc[[3, 5, 8], ['fare', 'age']])

# Task 6: Display the first three passengers and the first three columns

print(df.iloc[:3, :3])

# Task 7: Display the first three columns for every second passengers from 10 through 30

print(df.iloc[10:31:2, :3])

