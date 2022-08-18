# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:09:32 2020

@author: Andre Stevens
"""

import numpy as np

b = np.arange(6, dtype=float)
# print(b)

c = np.array([
    [4, 5, 6],
    [1, 2, 3]
    ])

d = np.array([
    [6, 2, -3],
    [14, -1, 6]
    ])

# print(c[0, 0])
# print(c[0][0])
# print(c[1])

# print(2 in c)
# print(5 in d)

# print(c+d)

print(np.dot(c, d))