#!STD
import matplotlib.pyplot as plt #!skip
import numpy as np #!skip
# Function to get complex plane
def get_complex_plane(start, stop, num):
    # Get arrays of xy arrays
    x_space = np.linspace(start[0], stop[0], int(num[0]))
    y_space = np.linspace(start[1], stop[1], int(num[1]))

    # Get meshgrids from arrays
    real, imag = np.meshgrid(x_space, y_space[::-1])

    # Setup complex plane
    c = np.zeros_like(real, dtype = np.cdouble)
    c.real = real
    c.imag = imag

    return c