import numpy as np

numArray = np.arange(1, 11).reshape((2, 5))
print("\n{}\n".format(numArray))

# EXAMPLE 1: Reshape review
reshArray = numArray.reshape((5, 2))
print("{}\n".format(reshArray))

# EXAMPLE 2: Using transpose()
transArray = numArray.transpose()
print("{}\n".format(transArray))