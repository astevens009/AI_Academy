import numpy as np

numArray = np.array([10, 20, 30, 40, 56, 60, 70, 80])
# print("\noriginal array: {}".format(numArray))

# EXAMPLE 1: Reverse the array
# revNumArray = np.flip(numArray)
# print("reversed array: {}\n".format(revNumArray))

# EXAMPLE 2: Reversing a 2D array
num2DArray = ([
    [2, 4, 6, 8, 10],
    [5, 10, 15, 20, 25],
    [10, 20, 30, 40, 50]
])

print("\noriginal 2D: {}\n".format(num2DArray))

# revNum2D = np.flip(num2DArray)
# print("reversed matrix: {}\n".format(revNum2D))

# EXAMPLE 3: Reverse the rows
# revRows = np.flip(num2DArray, axis=0)
# print("row reversal: {}\n".format(revRows))

# EXAMPLE 4: Reverse the columns
# revCols = np.flip(num2DArray, axis=1)
# print("column reversal: {}\n".format(revCols))

# EXAMPLE 5: Reversing a specific row
num2DArray2 = num2DArray.copy()
num2DArray2[2] = np.flip(num2DArray2[2])
print("reversed last row: {}\n".format(num2DArray2))
