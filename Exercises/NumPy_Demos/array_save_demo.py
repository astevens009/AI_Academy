import numpy as np

numArray = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
# print("\nOriginal array: {}\n".format(numArray))

# EXAMPLE 1: Save file as an .npy file
# np.save('tensArray', numArray)

# Load the array
# loadedArray = np.load('tensArray.npy')
# print("loaded array: {}\n".format(loadedArray))

# EXAMPLE 2: Saving as a .csv file
csvArray = numArray.copy()
np.savetxt('csvTensArray.csv', csvArray)

# loading the .csv array
print("\n{}\n".format(np.loadtxt('csvTensArray.csv')))