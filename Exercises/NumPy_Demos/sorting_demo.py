import numpy as np

numArray = np.array([2, 1, 5, 3, 4, 6, 8])
print("\nBefore: {}\n".format(numArray))

np.sort(numArray)
print("After: {}\n".format(np.sort(numArray)))