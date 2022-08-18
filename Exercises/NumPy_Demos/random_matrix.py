import numpy as np

# EXAMPLE 1: Generating a 2 x 4 matrix of random numbers from 0 to 4
randRng = np.random.default_rng(1)
randArray = randRng.integers(5, size=(2, 4), endpoint=True)

print("\n{}\n".format(randArray))
