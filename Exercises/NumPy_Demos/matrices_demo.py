import numpy as np

data = np.array([
    [5, 10],
    [15, 20]
])

# EXAMPLE 1:
print("\n{}\n".format(data))

# EXAMPLE 2: slicing
print("data[1:3] = {}\n".format(data[1:3]))
print("data[1:] = {}\n".format(data[1:]))
print("data[1:2] = {}\n".format(data[1:2]))
