import numpy as np

dataArray = np.array([2, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9])

# EXAMPLE 1: Distinct values
print("\nThe original array is: {}\n".format(dataArray))
distinct_values = np.unique(dataArray)
print("The distinct values are: {}\n".format(distinct_values))
