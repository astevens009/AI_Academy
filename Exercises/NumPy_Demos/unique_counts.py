import numpy as np

dataArray = np.array([2, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9])

# EXAMPLE 1: Distinct values
# print("\nThe original array is: {}\n".format(dataArray))
# distinct_values = np.unique(dataArray)
# print("The distinct values are: {}\n".format(distinct_values))

# EXAMPLE 2: Display the frequency of each of the elements in the array
# distinct_values, frequency = np.unique(dataArray, return_counts=True)
# print("The frequency of the values is: {} = {}".format(distinct_values, frequency))

# for index in distinct_values:
#     print("{} = {}".format(distinct_values[index], frequency[index]))

# EXAMPLE 3: Getting unique values from 2D arrays
numArray = np.array([
    [2, 4, 6, 8, 10, 12],
    [5, 10, 15, 20, 25, 30],
    [10, 20, 30, 40, 50, 60],
    [2, 4, 6, 8, 10, 12],
    [10, 20, 30, 40, 50, 60]
])

unique_nums = np.unique(numArray)
print("\nThe original array: {}\n\nThe unique data: {}\n"
      .format(numArray, unique_nums))

# EXAMPLE 4: Getting unique rows
unique_rows = np.unique(numArray, axis=0)
print("unique rows:\n{}\n".format(unique_rows))

# EXAMPLE 5: Getting unique rows index positions and frequency
unique_rows, indices, frequency = np.unique(
    numArray, axis=0, return_counts=True, return_index=True)

print("unique row(s):\n{}\n\nindices:\n{}\n\nfrequency:\n{}\n\n"
      .format(unique_rows, indices, frequency))
