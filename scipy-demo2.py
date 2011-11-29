import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scipy

fig = plt.figure()
ax = Axes3D(fig)

def lorenz_int(initial, t):
    x = initial[0]
    y = initial[1]
    z = initial[2]

    #
    sigma = 10
    rho = 28
    beta = 8.0/3
    x_dot = sigma * (y - x)
    y_dot = x * (rho -z) - y
    z_dot = x * y - beta* z
    
    return [x_dot, y_dot, z_dot]

initial = [0, 1, 1.05]

t = scipy.arange(0, 100, 0.01)
lorenz_sol = odeint(lorenz_int, initial, t)

x = [i[0] for i in lorenz_sol]
y = [i[1] for i in lorenz_sol]
z = [i[2] for i in lorenz_sol]

# ax.xlabel('x')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.plot(x, y, z)

plt.suptitle('$ x\' = \sigma(y-x) \hspace{1} y\' = x(\\rho - z) - y \hspace{1} z\'=xy - \\beta z  $')

plt.show()