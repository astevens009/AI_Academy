# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:35:57 2020

@author: Andre Stevens
@description: Working with tabular data
"""
import pandas as pd
import numpy as np

# NOTE: Titantic data retrieved from GitHub: https://github.com/pandas-dev/pandas/blob/master/doc/data/titanic.csv
# titanic_data = pd.read_csv("https://github.com/pandas-dev/pandas/blob/master/doc/data/titanic.csv")

titanic_data = pd.read_csv('titanic.csv')

# EXAMPLE 1: View DataFrame data
# print(titanic_data)
# print(titanic_data.head(10))

# EXAMPLE 2: Get the data types of the columns
# print(titanic_data.dtypes)

# EXAMPLE 3: Write data to a file (excel spreadsheet)
# titanic_data.to_excel('titanic_info.xlsx', sheet_name='passenger_info', index=False)

# EXAMPLE 4: Getting technical info
# print(titanic_data.info())
# print(type(titanic_data))   # display the type returned

# EXAMPLE 5: Filtering
# over_50 = titanic_data[titanic_data["Age"] > 50]
# print(over_50)

# # titanic_data[titanic_data["Age"] > 50].to_csv("over50.csv")

# print(over_50.shape)

# EXAMPLE 6 More filtering
# psgr_class_2_3 = titanic_data[titanic_data["Pclass"].isin([2, 3])]
# print(psgr_class_2_3)

# psgr_2_class = titanic_data[titanic_data["Pclass"].isin([2])]
# print(psgr_2_class)

# EXAMPLE 7: Selecting specific rows and columns
names_over50 = titanic_data.loc[titanic_data["Age"] > 50, "Name"]
print(names_over50)

# EXAMPLE 8: Selecting specific rows or columns by number
# Using iloc[...]
anonymous = titanic_data.iloc[0:3, 3]
print(anonymous)