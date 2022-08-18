import numpy as np

dataArray = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# EXAMPLE 1: Creating a new array from a slice
# sub_array = dataArray[2:5]
# print("\nsub array: {}\n".format(sub_array))

# EXAMPLE 2: Stacking arrays vertically (vstack)
# array1 = np.array([
#     [10, 20],
#     [30, 40]
# ])

# array2 = np.array([
#     [5, 10],
#     [15, 20]
# ])

# vertArray = np.vstack((array1, array2))
# print("\n{}\n".format(vertArray))

# EXAMPLE 2: Stacking arrays horizontally (hstack)
# array1 = np.array([
#     [10, 20],
#     [30, 40]
# ])

# array2 = np.array([
#     [5, 10],
#     [15, 20]
# ])

# hzArray = np.hstack((array1, array2))
# print("\n{}\n".format(hzArray))

# EXAMPLE 3: Using hsplit - equally shaped result arrays
# tensArray = np.arange(10, 201, 10).reshape(2, 10)
# print("\n{}\n".format(tensArray))

# equalShape = np.hsplit(tensArray, 5)
# print("{}\n".format(equalShape))

# equalShape = np.hsplit(tensArray, 10)
# print("{}\n".format(equalShape))

# EXAMPLE 4: Splitting the arrays on columns
# tensArray = np.arange(10, 201, 10).reshape(2, 10)
# print("\n{}\n".format(tensArray))

# colSplit = np.hsplit(tensArray, (4, 5))
# print("Splitting on the 4th and 5th column\n{}\n".format(colSplit))

# EXAMPLE 5: Demonstrating view()
# The following will change the original array using the view() function
numArray = np.array([
    [10, 20, 30, 40, 50],
    [60, 70, 80, 90, 100],
    [5, 10, 15, 20, 25]
])
print("\nnumArray: {}\n".format(numArray))

# numArray2 = numArray[2, :]
# print("numArray2: {}\n".format(numArray2))

# # NOTE: The following will modify the original array as well
# print("Modifying numArray2...\n")
# numArray2[2] = 30

# print("numArray: {}\n".format(numArray))
# print("numArray2: {}\n".format(numArray2))

# EXAMPLE 6: copy()
numArray3 = numArray.copy()
print("numArray3: {}\n".format(numArray3))

# NOTE: The following will modify the original array as well
print("Modifying numArray3...\n")
numArray3[2, 3] = 50

print("numArray: {}\n".format(numArray))
print("numArray3: {}\n".format(numArray3))