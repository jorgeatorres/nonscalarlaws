# encoding: utf-8
import time

import numpy as np
from pylab import *


def u0(x):
    if x <= 0.:
        return 1.
    elif x >= 1.:
        return 0.
    else:
        return 1. - x
        
def u(x,t):
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

ion()

x = linspace(-0.5, 1.5, 100)
t = np.r_[0.:1.1:0.05]

for i, ti in enumerate(t):
    clf()
    plot(x, [u(xi, ti) for xi in x], label='u(x, %0.2lf)' % ti)
    ylabel('u(x,t)')
    xlabel('x')
    ylim([0., 1.5])
    gca().grid(True)
    legend()
    draw()
    time.sleep(0.05)

ioff()
show()