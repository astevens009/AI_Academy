import numpy as np

# EXAMPLE 1: 
# array1 = np.array([[1, 2, 3, 4],
#                    [2, 4, 6, 8],
#                    [1, 3, 5, 7],
#                    [5, 10, 15, 20]
#                    ])

# print("\nThe third element in the array is: {}\n".format(array1[2]))

# print("The full array is:\n{}\n".format(array1))

# EXAMPLE 2: A 1-D array
# array_list = [5, 10, 15, 20, 25]
# array2 = np.array(array_list)

# print("\nThe full array is:\n{}\n".format(array2))

# EXAMPLE 3: An array filled with 0's or 1's
# print(np.zeros(4))
# print(np.ones(5))

# EXAMPLE 4: An empty array
# print(np.empty(5))   # the contents are random

# EXAMPLE 5: An array with a range of elements
# print(np.arange(5))

# EXAMPLE 6: Using np.linspace()
# print(np.linspace(1, 15, num=5))

# EXAMPLE 7: Specifying a data type
print(np.arange(5, dtype=np.float))
print(np.arange(1, 10, dtype=np.float))