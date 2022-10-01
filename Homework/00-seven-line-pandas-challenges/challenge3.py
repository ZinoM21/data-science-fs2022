import seaborn as sns
df = sns.load_dataset('titanic')

# Task 1: Display the survived passengers

print(df[df['survived'] == 1])

# Task 2: Display the 2nd class passengers

print(df[df['pclass'] == 2])

# Task 3: Display the infants (age 1 or younger)

print(df[df['age'] <= 1])

# Task 4: Display children between 10 and 13

print(df[(df['age'] >= 10) & (df['age'] <= 13)])

# Task 5: Display survived 2nd class passengers

print(df[(df['survived'] == 1) & (df['pclass'] == 2)])

# Task 6: Find at least one female passenger who embarked in Cherbourg and is 40-50 years old



# Task 7: Display the passengers that do not have a missing age