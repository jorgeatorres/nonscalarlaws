import numpy as np
import scipy.integrate

def godunov(u0, flux, riemann_solver, x0, xI, t0, tN, dx, dt):
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
                if i == 0 or i == len(x) - 1:
                    u[n,i] = u[n-1,i]
                else:
                    lflux = flux(riemann_solver(u[n-1,i-1], u[n-1,i]))
                    rflux = flux(riemann_solver(u[n-1,i], u[n-1,i+1]))
                    
                    u[n,i] = u[n-1,i] - ((dt / dx) * (rflux - lflux))
                    
        
    return (u, x, t)

    

