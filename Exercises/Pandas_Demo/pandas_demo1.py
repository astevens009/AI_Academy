# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 14:29:22 2020

@author: A. Stevens
Descritption: Demonstration of Pandas
"""
import pandas as pd
import numpy as np

data = {'one': [1., 2., 3., 4.],
        'two': [4., 3., 2., 1.],
        'three': [5., 6., 7., 8.]}

dataFrame = pd.DataFrame(data)
