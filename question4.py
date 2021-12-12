import math
import numpy as np
from matplotlib import pyplot as plt
fig = plt.figure()
ax = plt.gca()

ax.set_aspect(1)

x=np.linspace(0, 0, 100000)
y=np.linspace(0, 0, 100000)
for i in range(0,100000):
    x[i] = np.random.uniform(-5,5.0)
    y[i] = np.random.uniform(-5,5.0)
X=np.linspace(0, 0, 10000)
Y=np.linspace(0, 0, 10000)
Z=np.linspace(0, 0, 10000)
Z0=np.linspace(-100, 100, 10000)
for i in range(0,10000):
    for j in range(0,10):
        X[i] += x[10 * i + j]
        Y[i] += y[10 * i + j]
        Z[i] =X[i]+Y[i]

plt.xlim(-50,50)
plt.ylim(-50,50)
plt.scatter(X,Y,s=0.1,c='red')
# plt.xlim(-100,100)
# plt.ylim(-100,100)
# plt.scatter(Z,Z0,s=0.1,c='red')
plt.show()

