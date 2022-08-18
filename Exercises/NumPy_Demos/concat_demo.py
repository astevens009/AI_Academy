import numpy as np

array1 = np.array([1, 3, 5, 7])
array2 = np.array([2, 4, 6, 8])

# EXAMPLE 1: Concatenating arrays
# print(np.concatenate((array1, array2)))

# EXAMPLE 1a: Concatenate then sort
# print(np.sort(np.concatenate((array1, array2))))

# EXAMPLE 2: Concatenate using axis parameter
coord1 = np.array([[1, 2], [3, 4]])
coord2 = np.array([[5, 6]])

# print(np.concatenate((coord1, coord2), axis=0))
print(np.concatenate((coord1, coord2)))
