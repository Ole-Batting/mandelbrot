import cv2
import numpy as np
from utils import *

if __name__ == '__main__':

    k = 216
    aspect_ratio = 16/9
    resolution = np.array([aspect_ratio * k, k], dtype = int)

    center = np.array([-0.5, 0.0], dtype = float)
    radius = np.array([aspect_ratio, 1], dtype = float)
    start = center - radius
    stop = center + radius

    maxiter = 40
    last_maxiter = 0
    mod = 40
    cmap = 19

    redo_space = True
    redo_iter = True
    redo_image = True

    cv2.namedWindow("Mandelbrot")
    cv2.setMouseCallback("Mandelbrot", on_mouse)
    
    while True:
        if redo_space:
            c = get_complex_plane(start, stop, resolution)

        if redo_iter:
            escape = apply_n_times2(np.zeros_like(c), c, last_maxiter, maxiter, np.zeros_like(c, dtype = float))
        
        if redo_image:
            image = make_image_nice(escape, mod, cmap)
            cv2.imshow("Mandelbrot", image)

        print(f"section [[{start[0]},{start[1]}],[{stop[0]},{stop[1]}]]\nmaxiter {maxiter}")
        print(f"cmap {cmap}\nres {resolution}\n")

        # setup for next iteration
        redo_space = True
        redo_iter = True
        redo_image = True
        last_maxiter = 0

        key = cv2.waitKey() & 0xFF

        if key == ord("q"):
            cv2.destroyAllWindows()
            break

        elif key == ord("s"):
            x_str = f"{str(start[0]).replace('.','_')}-{str(stop[0]).replace('.','_')}"
            y_str = f"{str(start[1]).replace('.','_')}-{str(stop[1]).replace('.','_')}"
            cv2.imwrite(f"output/x-{x_str}-y-{y_str}-m-{maxiter}-c-{cmap}-{mod}.png", image)
            redo_space = False
            redo_iter = False
            redo_image = False

        elif key == ord("e"):
            # extend maxiter
            last_maxiter = maxiter
            maxiter *= 2
            redo_space = False
        
        elif key == ord("d"):
            # decrease maxiter
            last_maxiter = 0
            maxiter //= 2
            redo_space = False
            redo_iter = False
            redo_image = False

        elif key == ord("c"):
            # change colormap
            cmap += 1
            cmap %= 22
            redo_space = False
            redo_iter = False

        elif key == ord("z"):
            # zoom in
            radius /= 2
            print('radius', radius)
            start = center - radius
            stop = center + radius

        elif key == ord("x"):
            # zoom out
            radius *= 2
            print('radius', radius)
            start = center - radius
            stop = center + radius

        elif key == ord("+"):
            # increase image size
            k = int(k * 1.2)
            resolution = np.array([aspect_ratio * k, k])

        elif key == ord("-"):
            # decrease image size
            k = int(k / 1.2)
            resolution = np.array([aspect_ratio * k, k])

        elif key == ord('w'):
            # re-center
            c_point = c[coords[-1][1], coords[-1][0]]
            center[0] = c_point.real
            center[1] = c_point.imag
            start = center - radius
            stop = center + radius
            print('center', center[0], center[1])