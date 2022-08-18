# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:32:40 2020

@author: Andre Stevens

@description: Slicing and indexing in NumPy
"""

import numpy as np

fives_data = np.array([5, 10, 15, 20, 25, 30])
dataArray = np.array([
    [5, 10, 15, 20, 25, 30],
    [2, 4, 6, 8, 10, 12],
    [3, 6, 9, 12, 15, 18]
    ])

target = 10

# EXAMPLE 1:
print(fives_data[0:3])    # display the fist 3 elements
print(fives_data[:4])
print(fives_data[2:4])

# EXAMPLE 2: Getting all values less than a given amount

# TODO: Determine if there is a way to get distinct values
# print(np.sort(dataArray[dataArray < target]))

# EXAMPLE 3: Get all numbers greater than or equal to target
# target = (dataArray >= 5)
# print("The numbers greater than or equal to 5 are: {}".format(dataArray[target]))

# EXAMPLE 4: Get all numbers divisible by 2
# divisible_by_2 = dataArray[dataArray%2==0]
# print("The numbers divisible by 2 are: {}".format(divisible_by_2))

# EXAMPLE 5: Multiple criterion...
# sample_range = dataArray[(dataArray > 3) & (dataArray < 10)]
# print(np.sort(sample_range))

# EXAMPLE 6: Using np.nonzero() to print the indices of elements 
# less than 5
# lt_five = np.nonzero(dataArray < 5)
# print("\nIndices of elements less than 5: {}\n".format(lt_five))

# EXAMPLE 6a: Using zip()
# print(list(zip(lt_five)))

# print("Coordinates:")
# array_coords = list(zip(dataArray[0], dataArray[1], dataArray[2]))
# for coord in array_coords:
#     print(coord)

# EXAMPLE 7: Using np.nonzero() to print elements in the array
# lt_five = np.nonzero(dataArray < 5)
# print("Elements less than 5: {}\n".format(dataArray[lt_five]))

# EXAMPLE 8: Return an empty array of indices
# target = 50
# empty_array = np.nonzero(dataArray == target)
# print("Target: {}\nEmpty sample: {}".format(target, empty_array))