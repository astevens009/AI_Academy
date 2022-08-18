# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:40:24 2020

@author: AndreS009
"""

import pandas as pd
import numpy as np

captainDataFrame = pd.DataFrame({
    "Name": ["Malcolm Reynolds",
                     "Benjamin Sisko",
                     "Morpheus"],
    "Rank": ["Captain", 
             "Captain",
             "Captain"],
    "Ship": ["Serenity",
             "Defiant",
             "Nebudchanezzer"],
    "Missions": [102,
                 374,
                 219]
    })

# EXAMPLE 1: Display the dataframe
# print(captainDataFrame)

# EXAMPLE 2: Displaying a column (or Series)
names = captainDataFrame["Name"]
# print(names)

# EXAMPLE 2: Find the captain with the most missions
# maxMissions = captainDataFrame["Missions"].max()
# print("\nThe most missions flown is: {}".format(maxMissions))

# Using max() on the Series
# missions = captainDataFrame["Missions"]
# print("\nSERIES: The most missions is: {}".format(missions.max()))

# EXAMPLE 3: Using the describe() function
print(captainDataFrame.describe())