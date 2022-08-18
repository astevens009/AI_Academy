import numpy as np
import matplotlib.pyplot as plt
import random as r

# Using different ranges to create a pseudo
# skewed distribution of numbers
data = [r.randint(25, 50) for i in range(100)]
data += [r.randint(1, 25) for i in range(50)]
data += [r.randint(51, 100) for i in range(40)]

plt.hist(data, bins=10)
plt.show()