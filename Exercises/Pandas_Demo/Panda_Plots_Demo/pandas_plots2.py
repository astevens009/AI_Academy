# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:42:22 2020

@author: A. Stevens
@description: Creating new columns derived from existing columns
"""
import pandas as pd

air_quality = pd.read_csv("air_quality_no2.csv", 
                          index_col=0, parse_dates=True)
# print(air_quality.head())

# EXAMPLE 1: Express the NO2 concentration of the London station in mg/m^3
# Assuming a temperature of 25 degrees C abd a pressure of 1013 hPa (hectopascal)

# EXAMPLE 2: Checking the ratio of values in Paris vs Antwerp, saving the result in a new column
# air_qual = air_quality["ratio_paris_antwerp"] = \
#     air_quality["station_paris"] / air_quality["station_antwerp"]
# air_qual.to_csv("paris_antwerp_ratio.csv")
# print(air_quality.head())

# EXAMPLE 3: Renaming data columns
# Using station identifiers used by openAQ
air_quality_renamed = air_quality.rename(columns={
    "station_antwerp": "BETR801",
    "station_paris": "FR04014",
    "station_london": "London Westminster"
    })
print(air_quality_renamed.head())