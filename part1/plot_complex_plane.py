#!STD
import matplotlib.pyplot as plt #!skip
import numpy as np #!skip
from setup import * #!skip
from complex_plane import * #!skip
# Plot real and imaginary parts of complex plane
c = get_complex_plane(start, stop, num)
fig, ax = plt.subplots(1, 2, figsize=(12,6))

im = ax[0].imshow(c.real)
ax[0].set_title('Real part')
plt.colorbar(im)

im = ax[1].imshow(c.imag)
ax[1].set_title('Imaginary part')
plt.colorbar(im)

plt.show()