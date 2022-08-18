import numpy as np

array_example = np.array([
    [
        [0, 1, 2, 3],
        [4, 5, 6, 7]
    ],
    [
        [2, 4, 6, 8],
        [1, 3, 5, 7]
    ],
    [
        [5, 10, 15, 20],
        [4, 8, 12, 16]
    ]
])

# EXAMPLE 1: get the dimention of the array
# print("\nThe dimension of the array is: {}\n".format(array_example.ndim))

# EXAMPLE 2: get the number of elements
# print("The size of the array is: {}\n".format(array_example.size))

# EXAMPLE 3: get the shape of the array
# print("The shape of the array is: {}\n".format(array_example.shape))

# EXAMPLE 4: reshaping an array
# numArray = np.arange(6)
# print("\n{}\n".format(numArray))

# changeShapeArray = numArray.reshape(3, 2)
# print("\n{}\n".format(changeShapeArray))

# EXAMPLE 4a:
print("\n{}\n".format(array_example.reshape(8, 3)))
print("{}\n".format(array_example.reshape(6, 4)))