# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:12:26 2020

@author: Andre Stevens
"""

import pandas as pd

titanic_data = pd.read_csv("titanic.csv")
print(titanic_data[["PassengerId", "Survived", "Pclass", "Name"]].head())