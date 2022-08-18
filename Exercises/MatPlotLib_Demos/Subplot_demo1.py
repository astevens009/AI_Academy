# -*- coding: utf-8 -*-
"""
MatPlotLib Tutorial - Subplots
Created on Tue Dec  8 16:28:53 2020

@author: A. Stevens
"""

import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [1, 2, 4, 3]

# EXAMPLE 1: Creating plots and subplots
# fig, ax = plt.subplots(1, 2)
# plt.plot(x, y)  # don't do this

# Remember that subplots() returns a fig and ax
# so instead do this:
    
# ax[0].plot(x, y)
# ax[1].scatter(x, y)

# # EXAMPLE 2: Labelling
# ax[0].set_xlabel("Plot 1")
# ax[1].set_xlabel("Plot 2")

# EXAMPLE 3: Working with multi-dimensional subplots
# fig, ax = plt.subplots(2, 3)

# ax[0, 0].plot(x, y)
# ax[0, 1].scatter(x, y)

# # EXAMPLE 3a: Superimposing subplots
# ax[0, 2].plot(x, y)
# ax[0, 2].scatter(x, y)

# EXAMPLE 4: Displaying/hiding tick marks
fig, ax = plt.subplots(2, 3, sharex=True, sharey=True)

ax[0, 0].plot(x, y)
ax[0, 1].scatter(x, y)

# EXAMPLE 3a: Superimposing subplots
ax[0, 2].plot(x, y)
ax[0, 2].scatter(x, y)