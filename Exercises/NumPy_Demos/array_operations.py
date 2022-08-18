import numpy as np

array1 = np.array([10, 20, 30])
array2 = np.array([5, 10, 15])

# EXAMPLE 1: Adding arrays
# print("\narray1: {}".format(array1))
# print("array2: {}\n".format(array2))
# sumArray = array1 + array2
# print("The sum of the arrays is: {}\n".format(sumArray))

# EXAMPLE 2: Math operations
# print("=" * 40)
# print("Additional aritmetic operations...")
# print("The difference: {}".format(array1 - array2))
# print("The product: {}".format(array1 * array2))
# print("The quotient (float): {}".format(array1 / array2))
# print("The quotient (int): {}\n".format(array1 // array2))

# EXAMPLE 3: Functions to perform basic math operations
# print("=" * 40)
# numArray = np.array([2, 4, 6, 8, 10])
# print("\nnumArray = {}".format(numArray))

# print("The sum of the elements in numArray = {}\n".format(numArray.sum()))

# EXAMPLE 4:  Finding the sum along axis = 1
numArray = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

numArray2 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 1, 13, 14, 15]
])

# print("column sum: {}\n".format(numArray.sum(axis = 1)))
# print("column2 sum: {}\n".format(numArray2.sum(axis = 1)))

# # EXAMPLE 5: Finding the sum along axis = 0
# print("row sum: {}\n".format(numArray.sum(axis = 0)))
# print("row sum: {}\n".format(numArray2.sum(axis = 0)))