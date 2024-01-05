#!STD
import matplotlib.pyplot as plt
import numpy as np

# Settings
k = 200
center = np.array([-0.5, 0.0])
radius = np.array([1.5, 1.0])
num = np.array([3, 2]) * k
maxiter = 40

# Extends
start = center - radius
stop = center + radius