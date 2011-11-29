# encoding: utf-8
import numpy as np
import scipy.integrate

np.seterr(all='raise')

def laxfriedrichs(u0, flux, x0, xI, t0, tN, dx, dt):
    x = np.r_[x0:xI + dx:dx]
    t = np.r_[t0:tN + dt:dt]
    
    u = np.zeros([len(t), len(x)])
    
    for n in xrange(0, len(t)):
        if n == 0:
            # initial condition
            for i, xi in enumerate(x[:-1]):
                u[0,i] = (1. / dx) * scipy.integrate.quad(u0, x[i], x[i+1])[0]
            u[0,-1] = u0(x[-1])
        else:
            for i in xrange(0, len(x)):
                if i == 0:
                    u[n,i] = u[n-1,i]
                elif i == len(x) - 1:
                    u[n,i] = u[n-1, i]
                else:
                    _m = (0.5 * (u[n-1,i-1] + u[n-1,i])) - ((flux(u[n-1,i]) - flux(u[n-1,i-1])) * (dt / dx) * 0.5)
                    _M = (0.5 / dx) * ((dx * (u[n-1,i] + u[n-1,i+1])) - ((flux(u[n-1,i+1]) - flux(u[n-1,i])) * dt))
                    
                    u[n,i] = 0.5 * (_m + _M - ((flux(_M) - flux(_m)) * (dt / dx)))
        
    return (u, x, t)