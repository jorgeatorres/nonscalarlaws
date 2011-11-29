# encoding: utf-8
import time
import numpy as np
import pylab as pl

from methods.laxfriedrichs import laxfriedrichs

# Lax-1 - Burger's eq. (convex flux)

def uexact(x,t):
    if t == 0.: return u0(x)
    
    if t < 1.:
        if t >= x:
            return 1.
        elif t <= x and x <= 1.:
            return (1 - x) / (1 - t)
        elif 1. <= x:
            return 0.
    else:
        return 1. if (1 + t > (2*x)) else 0.

def u0(x):
    if x <= 0.:
        return 1.
    elif x >= 1.:
        return 0.
    else:
        return 1. - x
        
def u0b(x):
    return np.sin(2 * np.pi * x)

def ex1():
    dx = 0.05
    dt = 0.025
    return laxfriedrichs(u0, lambda u: u*u, -0.5, 1.0, 0., 0.8, dx, dt)
    
u, x, t = ex1()

# 
pl.ion()

for j, tj in enumerate(t):
    pl.clf()
    pl.xlim([x[0], x[-1]])
    pl.ylim(0., 1.5)

    # pl.plot(x, [uexact(xi, tj) for xi in x], 'b')
    pl.plot(x, u[j], '.-r')
    
    pl.gca().grid(True)
    pl.draw()
    time.sleep(0.002)
    
pl.ioff()
pl.show()