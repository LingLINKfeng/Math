import math

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# matplotlib.rc('text', usetex=True)
# matplotlib.rcParams['text.latex.preamble']=[r"\usepackage{amsmath}"]

fig = plt.figure()
ax = plt.gca()

#-- Set axis spines at 0
for spine in [ 'bottom']:
    ax.spines[spine].set_position('zero')
#-- Hide the other spines...
for spine in ['left','right', 'top']:
    ax.spines[spine].set_color('none')
#-- Decorate the spines
arrow_length = 40 # In points
#-- X-axis arrow
# ax.annotate('$v$', xy=(0, 0.05), xycoords=('data', 'axes fraction'),
#             xytext=(0,arrow_length*2 ), textcoords='offset points',
#             ha='center', va='bottom',
#             arrowprops=dict(arrowstyle='-|>', fc='green'))
# #-- Y-axis arrow
# ax.annotate('$v$', xy=(0, 0.4), xycoords=('data', 'axes fraction'),
#             xytext=(-50, arrow_length*2), textcoords='offset points',
#             ha='center', va='bottom',
#             arrowprops=dict(arrowstyle='-|>', fc='black'))
#-- Plot
#ax.axis([-4*np.pi, 4*np.pi, -7.2, +7.2])
ax.grid(False)
ax.set_aspect(1)

# Turn off ticks
ax.set_yticks([])
ax.set_xticks([])

# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([])

#-- Function
theta=np.arange(0, np.pi, 0.01)
X = np.linspace(-3, 2, 6)

q3=math.sqrt(3)
#light from above
xlup=[-3,-6]
ylup=[0,q3]

xrup=[3,-3]
yrup=[0,2*q3]
#light after refraction
xldown=[-3,1]
yldown=[0,-4*q3]

xrdown=[3,6]
yrdown=[0,-3*q3]
#up line

#up
px1=[-3,-6/4];py1=[0,6*q3/4]
px2=[-2,-3/4];py2=[0,5*q3/4]
px3=[-1,   0];py3=[0,4*q3/4]
px4=[ 0, 3/4];py4=[0,3*q3/4]
px5=[ 1, 6/4];py5=[0,2*q3/4]
px6=[ 2, 9/4];py6=[0,1*q3/4]
#down
px1d=[ 12/4,-6/4];py1d=[0/4,-6*q3/4]
px2d=[ 14/4,-4/4];py2d=[-q3*2/4,-8*q3/4]
px3d=[ 16/4,-2/4];py3d=[-q3*4/4,-10*q3/4]
px4d=[ 18/4,-0/4];py4d=[-q3*6/4,-12*q3/4]
px5d=[ 20/4,2/4];py5d=[-q3*8/4,-14*q3/4]
# px2d=[-2,-3/4];py2d=[0,5*q3/4]
# px3d=[-1,   0];py3d=[0,4*q3/4]
# px4d=[ 0, 3/4];py4d=[0,3*q3/4]
# px5d=[ 1, 6/4];py5d=[0,2*q3/4]
# px6d=[ 2, 9/4];py6d=[0,1*q3/4]

r1=[-1/2]
r2=[-1/2,-1]
r3=[-1/2,-1,-3/2]
r4=[-1/2,-1,-3/2,-2]
r5=[-1/2,-1,-3/2,-2,-5/2]
r6=[-1/2,-1,-3/2,-2,-5/2,-3]
for r in r1:
    pointX=X[5]+r*np.cos(theta)
    pointY = r * np.sin(theta)
    plt.plot(pointX, pointY, 'g')
for r in r2:
    pointX=X[4]+r*np.cos(theta)
    pointY = r * np.sin(theta)
    plt.plot(pointX, pointY, 'g')
for r in r3:
    pointX=X[3]+r*np.cos(theta)
    pointY = r * np.sin(theta)
    plt.plot(pointX, pointY, 'g')
for r in r4:
    pointX=X[2]+r*np.cos(theta)
    pointY = r * np.sin(theta)
    plt.plot(pointX, pointY, 'g')
for r in r5:
    pointX=X[1]+r*np.cos(theta)
    pointY = r * np.sin(theta)
    plt.plot(pointX, pointY, 'g')
for r in r6:
    pointX=X[0]+r*np.cos(theta)
    pointY = r * np.sin(theta)
    plt.plot(pointX, pointY, 'g')

for i in range(0,6):
    plt.scatter(X[i], 0, 15,c="#000000")

#plt.savefig("wavefront propagation.png", dpi=1200, bbox_inches='tight')
plt.plot(xlup, ylup, color='r')
plt.plot(xrup, yrup, color='r')
plt.plot(xldown, yldown, color='blue')
plt.plot(xrdown, yrdown, color='blue')

plt.plot(px1, py1, color='r', ls="--")
plt.plot(px2, py2, color='r', ls="--")
plt.plot(px3, py3, color='r', ls="--")
plt.plot(px4, py4, color='r', ls="--")
plt.plot(px5, py5, color='r', ls="--")
plt.plot(px6, py6, color='r', ls="--")

plt.plot(px1d, py1d, color='blue', ls="--")
plt.plot(px2d, py2d, color='blue', ls="--")
plt.plot(px3d, py3d, color='blue', ls="--")
plt.plot(px4d, py4d, color='blue', ls="--")
plt.plot(px5d, py5d, color='blue', ls="--")
plt.show()

def calculate_circle_coordinate(center_x, center_y, radius, angle):
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    return x, y