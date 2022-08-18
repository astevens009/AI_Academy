# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:13:46 2020

@author: A. Stevens
@description: How to reshape the layout of tables
"""
import pandas as pd
titanic_data = pd.read_csv("titanic.csv")
aq_data = pd.read_csv("air_quality_long.csv",
                      index_col="date.utc", 
                      parse_dates=True)

# print(titanic_data.head())
# print(aq_data.head())

# EXAMPLE 1: Sorting table rows
# print(titanic_data[["PassengerId", "Survived", "Pclass", "Age"]].sort_values(by="Age").head())

# # Sort descending
# print(titanic_data[["PassengerId", "Survived", "Pclass", "Age"]].sort_values(by="Age", ascending=False).head())

# EXAMPLE 2: Sort by cabin class and age
# print(titanic_data[["PassengerId", "Survived", "Pclass", "Age"]].sort_values(by=["Pclass", "Age"], ascending=False).head())

# EXAMPLE 3: Using a subset of the dataset (air quality)
# Filtering for NO2 data only
no2 = aq_data[aq_data["parameter"] == "no2"]

# #Use 2 measurements (head) for each location (groupby)
#no2_subset = no2.sort_index().groupby(["location"]).head(2)
# print(no2_subset)
# no2_subset.to_csv("no2_subset.csv")

# EXAMPLE 4: Values as separate columns
# print(no2_subset.pivot(columns="location", values="value"))

# EXAMPLE 5: Plotting multiple columns
# print(no2.head())
# print(no2.pivot(columns="location", values="value").plot())

# EXAMPLE 6: Using pivot_table()
# aq_mean = aq_data.pivot_table(values="value", index="location",
#                               columns="parameter", aggfunc="mean")
# print("\n{}\n".format(aq_mean))

# EXAMPLE 7: Using pivot_table() with summary
# print(aq_data.pivot_table(values="value", index="location",
#                     columns="parameter", aggfunc="mean", 
#                     margins=True))

# EXAMPLE 8: Wide to long format
# Reset the table
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()
print(no2_pivoted.head())




