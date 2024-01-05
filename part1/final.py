#!STD
import matplotlib.pyplot as plt #!skip
import numpy as np #!skip
from setup import * #!skip
from complex_plane import * #!skip
from apply import * #!skip
# Calculate Mandebrot set
c = get_complex_plane(start, stop, num)
escape = apply_n_times(np.zeros_like(c), c, maxiter)

# Plot Mandelbrot set
plt.imshow(escape)
plt.show()