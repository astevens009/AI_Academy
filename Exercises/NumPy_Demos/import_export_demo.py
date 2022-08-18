# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:16:46 2020

@author: Andre Stevens
"""

import pandas as pd
import numpy as np

# EXAMPLE 1: reading a .csv file
# data = pd.read_csv('crewRoster.csv', header=0).values
# print(data)

# EXAMPLE 2: selecting specific columns
# data = pd.read_csv('crewRoster.csv', usecols=['First Name', 'Last Name', 'Rank']).values
# print(data)

# EXAMPLE 3: Creating a data frame for an array
# numArray = np.array([
#     [2, 4, 6, 8, 10, 12],
#     [5, 10, 15, 20, 25, 30],
#     [10, 20, 30, 40, 50, 60]
#     ])

# numDatFrm = pd.DataFrame(numArray)

#print("\n{}\n".format(numDatFrm))

# EXAMPLE 4: Saving the datafame
# numDatFrm.to_csv('numdf.csv')

# EXAMPLE 5: Reading a saved dataframe
numData = pd.read_csv('numdf.csv')
print("{}\n".format(numData))