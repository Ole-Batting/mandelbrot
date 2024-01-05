#!STD
import numpy as np #!skip
# Applied function 
def f(z, c):
    return z ** 2 + c

# Function to apply multiple times
def apply_n_times(z, c, n):
    # Setup image of escape iterations
    escape = np.zeros_like(c, dtype = float)

    # Apply n times
    for _ in range(n):
        z = f(z, c)
        escape[np.abs(z) < 2] += 1

    return escape