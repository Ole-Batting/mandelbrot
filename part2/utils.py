import cv2
import matplotlib.pyplot as plt
import numpy as np

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

# Applied function 
def f(z, c):
    return z ** 2 + c

# Function to apply multiple times
def apply_n_times(z, c, n):
    # Setup image of escape iterations
    escape = np.zeros_like(c, dtype = float)
    
    # Apply n times
    for i in range(n):
        z = f(z, c)
        m = np.abs(z) < 2
        escape[m] += 1
        if np.sum(m) == 0:
            break
    return escape

def apply_n_times_parallel(c, n):
    # Setup image of escape iterations
    escape = np.zeros_like(c, dtype = float)
    
    # Apply n times
    z = np.zeros_like(c)
    for i in range(n):
        z = f(z, c)
        m = np.abs(z) < 2
        escape[m] += 1
        if np.sum(m) == 0:
            break
    return escape

# Function to apply multiple times
def apply_n_times2(z, c, last_n, n, escape):
    # Apply n times
    for _ in range(last_n, n):
        z = f(z, c)
        m = np.abs(z) < 2
        escape[m] += 1
        if np.sum(m) == 0:
            break
    return escape

# Mouse coordinated callback
coords = []
def on_mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        coords.append([x, y])
        print(x, y)
    
def make_image_nice(image, mod, cmap=cv2.COLORMAP_TWILIGHT_SHIFTED):
    # Get mandelbrot set
    mask = image == np.max(image)
    # Modulo image
    image %= mod
    # Scale values to 8bit image and convert type
    image = (255 / (mod - 1) * image).astype(np.uint8)
    # Colorize
    image = cv2.applyColorMap(image, cmap)
    # Color mandelbrot set black
    image[mask] = [0,0,0]
    return image

def smooth(arr, ws, overweight_factor = 1):
    if ws % 2 == 0:
        ws += 1
    smooth_arr = np.zeros_like(arr)
    for i in range(len(arr)):
        start = max(0, i - ws // 2)
        end = min(len(arr), i + ws // 2)
        n = end - start
        weight = np.ones((n))
        if start == 0:
            weight[0] += (ws - np.sum(weight)) * overweight_factor
        elif end == len(arr):
            weight[-1] += (ws - np.sum(weight)) * overweight_factor
        smooth_arr[i] = np.average(arr[start:end], weights=weight)
    return smooth_arr

def smooth_it(arr, ws, it, owf1 = 0, owf2 = 2):
    smooth_arr = arr.copy()
    for _ in range(it):
        smooth_arr[:ws // 2] = (arr[:ws // 2] + arr[0] * owf1) / (1 + owf1)
        smooth_arr[-ws // 2:] = (arr[-ws // 2:] + arr[-1] * owf1) / (1 + owf1)
        smooth_arr = smooth(smooth_arr, ws, owf2)
    return smooth_arr

def inter(fp, n, ws = 21, it = 5, owf1 = 2):
    m = len(fp)
    xp = np.arange(m)
    x = np.linspace(0, m-1, n)
    y = np.interp(x, xp, fp)
    return smooth_it(y, ws, it, owf1=owf1)
