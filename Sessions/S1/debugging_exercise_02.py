#!/usr/bin/env python
# coding: utf-8

# Debugging Exercise: Population Growth

# We want to plot the population growth of a few selected countries.
# 
# The CSV file contains the population in millions.
# 
# Fix five bugs in the analysis.

import pandas as pd
import matplotlib.pyplot as plt


#OLD: df = pd.read_csv('population.csv')
df = pd.read_csv('population.csv', sep=';')
df.head()

# drop empty column
#OLD: del df[1949]
del df['1949']

# drop rows with missing data
df.dropna(inplace=True) # could also do interpulation here (imputation)

#OLD: df = df.set_index('country', inplace=True) # changes the df, returns None # also, the inplace mutates the df. If there wouldn't be inplace, the df would be copied and the copy would be returned
df.set_index('country', inplace=True)
df.head(3)

#interesting countries
interesting_countries = ['Argentina', 'Ukraine', 'Vietnam', 'Zimbabwe']
countries = df.loc[interesting_countries]
countries

# tilt the table by 90°
timeline = countries.transpose()
timeline.head()

# why is this a terrible plot?
#fix: pandas is very strong with date!!
timeline.index = pd.to_datetime(timeline.index)

timeline.plot()
