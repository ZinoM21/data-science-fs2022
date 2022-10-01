import pandas as pd
import seaborn as sns
df = sns.load_dataset('penguins')

# Task 1: What is the total mass of all penguins?

print(df['body_mass_g'].sum())

# Task 2: How many penguins are from which island?

print(df['island'].value_counts())

# Task 3: What is the average body mass of each species?

print(df.groupby('species')['body_mass_g'].mean())

# Task 4: How long is the longest beak of each species?

print(df.groupby('species')['bill_length_mm'].max())

# Task 5: What is the mean of each numerical column, per species?

print(df.groupby('species').mean())

# Task 6: How many penguins are there for each species/sex combination?


# Task 7: What is the standard deviation of bill length and depth for each species/sex combination  