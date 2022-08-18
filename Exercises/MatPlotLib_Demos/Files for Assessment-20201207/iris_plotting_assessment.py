# YOU ONLY NEED TO MODIFY LINES 33 and 34, DO NOT CHANGE ANY OTHER LINES

import matplotlib.pyplot as plt
import csv

# We'll be plotting the different iris plants using separate lists
# so that we can adjust the visualization for each one
setosa_x_axis = []
setosa_y_axis = []
versicolor_x_axis = []
versicolor_y_axis = []
virginica_x_axis = []
virginica_y_axis = []
with open('iris.csv', 'r') as contents:
  # Skip header
  header = contents.readline()
  reader = csv.reader(contents)
  for sepal_len, sepal_width, petal_len, petal_width, species in reader:
    # Recall how lists operate a little different than data types like ints
    # or floats. Below creates a reference point to which list we want to
    # append to.
    if species == "setosa":
      x_axis = setosa_x_axis
      y_axis = setosa_y_axis
    elif species == "versicolor":
      x_axis = versicolor_x_axis
      y_axis = versicolor_y_axis
    else:
      x_axis = virginica_x_axis
      y_axis = virginica_y_axis

    # These is the ONLY lines you need to modify for this lab
    x_axis.append(petal_width)
    y_axis.append(petal_len)

msize = 40 # Increase marker size
plt.scatter(setosa_x_axis, setosa_y_axis, c="red", s=msize)
plt.scatter(versicolor_x_axis, versicolor_y_axis, c="green", s=msize)
plt.scatter(virginica_x_axis, virginica_y_axis, c="blue", s=msize)
plt.show()