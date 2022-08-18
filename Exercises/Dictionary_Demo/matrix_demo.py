# Description:
# Demonstrating a sparse matrix

# EXAMPLE 1: List of lists (inefficient method)
# matrix = [
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 0],
#     [0, 2, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 3, 0]
# ]

# EXAMPLE 2: Creating a matrix using a dictionary
# NOTE: Here we store only the rows and columns with non-zero values
matrixDict = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

print("Value = {}".format(matrixDict.get((0, 3), 0)))
print("Value = {}".format(matrixDict.get((0, 2), 0)))   # displays 0 if value is not in the dictionary