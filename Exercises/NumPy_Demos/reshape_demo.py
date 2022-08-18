# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 01:37:09 2020

@author: Andre Stevens
"""

import numpy as np

numArray = np.array([5, 10, 15, 20, 25, 30])
print("\n{}\n".format(numArray))
print("numArray shape: {}\n".format(numArray.shape))

# EXAMPLE 1: Adding a new axis; row vector
# numArray2 = numArray[np.newaxis, :]
# print("numArray2 shape: {}\n".format(numArray2.shape))
# print("{}\n".format(numArray2))

# EXAMPLE 2: column vector
# numArray3 = numArray[:, np.newaxis]
# print("numArray3 shape: {}\n".format(numArray3.shape))
# print("{}\n".format(numArray3))

# EXAMPLE 3: Expanding an array
# numArray4 = np.expand_dims(numArray, axis=1)
# print("numArray4: {}\n".format(numArray4.shape))
# print("{}\n".format(numArray4))

# numArray5 = np.expand_dims(numArray, axis=0)
# print("numArray5 shape: {}\n".format(numArray5.shape))
# print(numArray5)

# EXAMPLE 4: Adding an axis at index position 1
numArray6 = np.expand_dims(numArray, axis=1)
print("numArray6 shape: {}\nnumArray6: {}".format(numArray6.shape, numArray6))

# EXAMPLE 5: Adding an axis at position 0
numArray7 = np.expand_dims(numArray, axis=0)
print("numArray7 shape: {}\nnumArray7: {}".format(numArray7.shape, numArray7))

# Insert numAry into numArray?
# numAry = np.array([2, 4, 6, 8, 10, 12])
# numArray8 = np.expand_dim()