# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:05:47 2020

@author: A. Stevens
@description: Handling time series data
"""
import pandas as pd
import matplotlib.pyplot as plt

aq_no2 = pd.read_csv("air_quality_no2_long.csv")
aq_no2 = aq_no2.rename(columns={"date.utc": "datetime"})

# print(aq_no2.head())
# print(aq_no2.city.unique())

# EXAMPLE 1: Datetime properties demo
# Display all the dates and times
aq_no2["datetime"] = pd.to_datetime(aq_no2["datetime"])
# print(aq_no2["datetime"])

# EXAMPLE 2: Display start and end times
# start_date = aq_no2["datetime"].min()
# end_date = aq_no2["datetime"].max()
# print("Start date/time: {}\nEnd date/time: {}\n"
#       .format(start_date, end_date))

# EXAMPLE 3: Time/date arithmetic (result: a Timedelta object)
# print("Time lapse: {}\n".format(end_date - start_date))

# EXAMPLE 4: Adding a month column to the DataFrame
# aq_no2["month"] = aq_no2["datetime"].dt.month
# print(aq_no2.head())

# EXAMPLE 5: Getting the average NO2 concentration for 
# each day of the week for each of the measurement 
# locations
# avg_no2_concentration = \
#     aq_no2.groupby([aq_no2["datetime"].dt.weekday,
#                     "location"])["value"].mean()
    
# print(avg_no2_concentration)

# EXAMPLE 6: Plotting the data
# Plot the typical NO2 pattern during the day of our 
# time series of all stations together (i.e. - what is
# the average value for each hour of the day?)
# fig, axs = plt.subplots(figsize=(12, 4))
# aq_no2.groupby(aq_no2["datetime"].dt.hour)["value"]\
#     .mean().plot(kind="bar", rot=0, ax=axs)
    
# EXAMPLE 7: Using the DatetimeIndex
# no2 = aq_no2.pivot(index="datetime", columns="location", values="value")
# print(no2.head())

# # Use the DatetimeIndex to get values
# print(no2.index.year)
# print(no2.index.weekday)

# EXAMPLE 8: resample()
# no2 = aq_no2.pivot(index="datetime", columns="location",\
#                    values="value")
# monthly_max = no2.resample("M").max()
# print(monthly_max)

# EXAMPLE 9: Plotting and resample()
# Make a plot of the daily mean NO2 value in each of the stations
no2 = aq_no2.pivot(index="datetime", columns="location",\
                    values="value")

no2.resample("D").mean().plot(style="-o", figsize=(10, 5))


















