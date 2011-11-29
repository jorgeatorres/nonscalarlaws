import numpy as np
import pylab as plt

ITERATIONS = 100
DENSITY = 500 # warning: execution speed decreases with square of DENSITY

x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5

x, y = np.meshgrid(np.linspace(x_min, x_max, DENSITY), np.linspace(y_min, y_max, DENSITY))

c = x + 1j*y # complex grid
z = c.copy()
fractal = np.zeros(z.shape, dtype=np.uint8) + 255

for n in range(ITERATIONS):
    z *= z
    z += c

    mask = (fractal == 255) & (abs(z) > 10)
    fractal[mask] = 254 * n / float(ITERATIONS)

plt.imshow(np.log(fractal), extent=(x_min, x_max, y_min, y_max))
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()