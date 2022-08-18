# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:22:39 2020

@author: A. Stevens
@description: Calculating summary statistics
"""
import pandas as pd

titanic_data = pd.read_csv("titanic.csv")
# print(titanic_data.head())

# EXAMPLE 1: Computing the average age fo the passengers
# avg_age = titanic_data["Age"].mean()
# print("The average age of the Titanic passengers was: {}"
#       .format(avg_age))

# EXAMPLE 2: The medican age and ticket price
# median_age, median_fare = titanic_data[["Age", "Fare"]].median()
# print("Median Age: {}\nMedian Fare: {}".format(median_age, median_fare))

# EXAMPLE 3: Calculating aggregate stats for multiple columns
# print(titanic_data[["Age", "Fare"]].describe())

# EXAMPLE 4: Custom aggregate stats
# print(titanic_data.agg({
#     'Age': ['min', 'max', 'median', 'skew'],
#     'Fare': ['min', 'max', 'median', 'mean']
#     }))

# EXAMPLE 5: Aggregating stats grouped by category
# print(titanic_data[["Sex", "Age"]].groupby("Sex").mean())

# EXAMPLE 6: Number of passendgers in each cabin class
# print(titanic_data["Pclass"].value_counts())





