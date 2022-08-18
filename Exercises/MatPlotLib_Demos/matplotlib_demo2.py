# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:17:42 2020

@author: A. Stevens
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Create a figure containing single axes
# fig, ax = plt.subplots()

# Plot some data on the axes
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

# EXAMPLE: Plotting without specifying the axes
# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])

# EXAMPLE 1: Demonstrating object-oriented style
# x = np.linspace(0, 2, 100)

# NOTE: Even in the OO-style, we use '.pyplot.figure' to create the figure
# Create a figure an axes
# fig, ax = plt.subplots()    

# # Plot some data on the axes
# ax.plot(x, x, label = 'linear')   
# ax.plot(x, x**2, label = 'quadratic')
# ax.plot(x, x**3, label= 'cubic')

# # Add an x-label to the axes
# ax.set_xlabel('x label')

# # Add a y-label to the axes
# ax.set_ylabel('y label')

# # Add a title
# ax.set_title("Simple Plot")

# # Add a legend
# ax.legend()

# EXAMPLE 2: Using pyplot
# x = np.linspace(0, 2, 100)
# Plot some data on the axes
# plt.plot(x, x, label = 'linear')   
# plt.plot(x, x**2, label = 'quadratic')
# plt.plot(x, x**3, label= 'cubic')

# # Add an x-label to the axes
# plt.xlabel('x label')

# # Add a y-label to the axes
# plt.ylabel('y label')

# # Add a title
# plt.title("Simple Plot")

# # Add a legend
# plt.legend()

# EXAMPLE 3: Performance rendering
# Set up and create the data to plot
# y = np.random.rand(100000)
# y[50000:] *= 2
# y[np.geomspace(10, 50000, 400).astype(int)] = -1
# mpl.rcParams['path.simplify'] = True

# mpl.rcParams['path.simplify_threshold'] = 0.0
# plt.plot(y)
# plt.show()

# mpl.rcParams['path.simplify_threshold'] = 1.0
# plt.plot(y)
# plt.show()

# EXAMPLE 4: Splitting lines
mpl.rcParams['path.simplify_threshold'] = 1.0

# Setup, and create the data to plot
y = np.random.rand(100000)
y[50000:] *= 2
y[np.geomspace(10, 50000, 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['agg.path.chunksize'] = 0
plt.plot(y)
plt.show()

mpl.rcParams['agg.path.chunksize'] = 10000
plt.plot(y)
plt.show()