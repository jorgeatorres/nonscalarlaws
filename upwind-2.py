# encoding: utf-8
import time
import numpy as np
import pylab as pl

from methods.upwind import upwind_p, upwind_n

# Upwind - Burger's eq. (convex flux)

def uexact(x,t):
    if t == 0.: return u0(x)

    return u0(x + t)

def u0(x):
    return np.sin(2 * np.pi * x)


# cfl = 0.5
def ex1():
    dx = 0.025
    cfl = 0.5
    return upwind_p(u0, lambda u: -u, -0.5, 1., 0., 0.4, dx, cfl * dx)
    
# cfl = 1.1
def ex2():
    dx = 0.025
    cfl = 0.5
    return upwind_n(u0, lambda u: -u, -0.5, 1., 0., 0.4, dx, cfl * dx)


# u, x, t = ex1()
u, x, t = ex2()


pl.ion()

for j, tj in enumerate(t):
    pl.clf()
    pl.xlim([x[0], x[-1]])
    # pl.ylim(0., 2.)

    pl.plot(x, [uexact(xi, tj) for xi in x], 'b')
    pl.plot(x, u[j], '.-r')
    
    pl.gca().grid(True)
    pl.draw()
    time.sleep(0.01)
    
pl.ioff()
pl.show()