from math import sin, pi
from numpy import zeros, linspace
import numpy as np
import matplotlib.pyplot as plt

c = 356#wave velocity
L = 5#Length of the domain
n = 50#number of grid points
dt = 0.1#time step
tstop = 5#the stop time


x = linspace(0, L, n+1) # grid points in x dir
dx = L/float(n)

C2 = (c*dt/dx)**2 # help variable in the scheme
dt2 = dt**2

u3 = zeros(n+1) # NumPy solution array
u1 = u3.copy() # solution at t-2dt
u2 = u3.copy() # solution at t-dt

t = 0.0

for i in range(0,n):
    u1[i] = sin(2*(L*i/n+1)*pi/L)
for i in range(1,n-1):
    u2[i] = u1[i] - 1/2*C2*(u1[i+1] - 2*u1[i] + u1[i-1])
u2[0] = 0; u2[n] = 0

while t <= tstop:
    t_old = t
    t += dt
    # update all inner points:
    for i in range(1, n-1):
        u3[i] = -u1[i-1] + 2*u2[i] + C2*(u2[i+1] - 2*u2[i] + u2[i-1])
    # insert boundary conditions:
    u3[0] = 0
    u3[n] = 0

    # update data structures for next step
    u1 = u2.copy()
    u2 = u3.copy()

x = linspace(0, L, n+1)
plt.plot(x,u3,3,c='red')
plt.show()