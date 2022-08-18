import numpy as np

dataArray = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

print("\nOriginal array: {}\n".format(dataArray))

# EXAMPLE 1: Using flatten()
flatArray = dataArray.flatten()
# print("flattened array: {}\n".format(flatArray))

# EXAMPLE 1a: Changes to new array don't change the parent
# print("Changing flatArray...\n")
# flatArray[4] = 15

# print("Original array: {}\n".format(dataArray))
# print("flattened array: {}\n".format(flatArray))

# EXAMPLE 2: Using ravel() (changes mde to the new array will change the original array)
dataArray2 = dataArray.copy()

print("dataArray2: {}\n".format(dataArray2))

ravelArray = dataArray2.ravel()
print("Changing array...\n")
ravelArray[9] = 20

print("ravelled array: {}\n".format(ravelArray))
print("dataArray2: {}".format(dataArray2))