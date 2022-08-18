# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:52:18 2020

@author: A. Stevens
@description: Combining data from multiple tables
"""
import pandas as pd


# Nitrate Data
aq_no2 = pd.read_csv("air_quality_no2_long.csv",
                     parse_dates=True)
aq_no2 = aq_no2[["date.utc", "location", 
                 "parameter", "value"]]

# Particulate Matter Data
aq_pm25 = pd.read_csv("air_quality_pm25_long.csv",
                      parse_dates=True)
aq_pm25 = aq_pm25[["date.utc", "location", 
                 "parameter", "value"]]


# print("TEST:\n{}\n".format(aq_no2.head()))
# print("TEST:\n{}\n".format(aq_pm25.head()))

# EXAMPLE 1: Combine the measurements of two tables
aq_data = pd.concat([aq_pm25, aq_no2], axis=0)
# print(aq_data.head())

# Check the shape of each of the tables
# Particulate table
# print("Shape of the `air quality PM25` table: ",
#       aq_pm25.shape)

# # Nitrate table
# print("Shape of the `air quality NO2` table: ",
#       aq_no2.shape)

# # Combined tables
# print("Shape of the `air quality data` table: ",
#       aq_data.shape)

# EXAMPLE 2: Using sort on the resulting DataFrame
print(aq_data.sort_values("date.utc").head())














