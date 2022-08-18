import numpy as np

data = np.array([
    [0.45053314, 0.17296777, 0.34376245, 0.5510652],
    [0.54627315, 0.05093587, 0.40067661, 0.55645993],
    [0.12697628, 0.82485143, 0.26590556, 0.56917101]
    ])

# EXAMPLE 1: sum()
print("\ndata = {}\n".format(data))
print("The sum of the data is: {}\n".format(data.sum()))

# EXAMPLE 2: min()
print("The minimum value is: {}\n".format(data.min()))

# EXAMPLE 3: Minimum value along axis = 0
print("The minimum values are: {}\n".format(data.min(axis=0)))