# encoding: utf-8
import numpy as np
import scipy.integrate


def upwind_p(u0, flux, x0, xI, t0, tN, dx, dt):
    x = np.r_[x0:xI + dx:dx]
    t = np.r_[t0:tN + dt:dt]
    
    u = np.zeros([len(t), len(x)])
    
    for n, tn in enumerate(t):
        if n == 0:
            # initial condition
            for i, xi in enumerate(x[:-1]):
                u[0,i] = (1. / dx) * scipy.integrate.quad(u0, x[i], x[i+1])[0]
            u[0,-1] = u0(x[-1])
        else:
            for i in xrange(0, len(x)):
                rflux = flux(u[n-1,i])
                
                if i == 0:
                    # flux through the boundary x = x0
                    # lflux = (1. / dt) * scipy.integrate.trapz([flux(u[n,0]), flux(u[n-1,0])], x=[t[n-1], t[n]])
                    lflux = flux(u[n-1,0])
                else:
                    lflux = flux(u[n-1,i-1])

                u[n,i] = u[n-1,i] - ((dt / dx) * (rflux - lflux))

    return (u, x, t)


def upwind_n(u0, flux, x0, xI, t0, tN, dx, dt):
    x = np.r_[x0:xI + dx:dx]
    t = np.r_[t0:tN + dt:dt]
    
    u = np.zeros([len(t), len(x)])
    
    for n, tn in enumerate(t):
        if n == 0:
            # initial condition
            for i, xi in enumerate(x[:-1]):
                u[0,i] = (1. / dx) * scipy.integrate.quad(u0, x[i], x[i+1])[0]
            u[0,-1] = u0(x[-1])
        else:
            for i in xrange(0, len(x)):
                lflux = flux(u[n-1,i])
                
                if i == len(x) - 1:
                    # flux through the boundary x = xI
                    rflux = -u0(x[-1] + tn)
                else:
                    rflux = flux(u[n-1,i+1])

                u[n,i] = u[n-1,i] - ((dt / dx) * (rflux - lflux))

    return (u, x, t)