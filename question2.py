import numpy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#初始化画布
fig = plt.figure()

ax1=fig.add_subplot(2,1,1)
plt.xlim(-2, 2)
plt.ylim(-4, 3)
t=np.arange(0,800,1)
Xpoint1=[]
Ypoint1=[]
Xpoint2=[]
Ypoint2=[]
Xpoint3=[]
Ypoint3=[]
Xpoint4=[]
Ypoint4=[]
Xpoint5=[]
Ypoint5=[]
for i in range(len(t)):
    Xpoint1.append(np.random.uniform(-2,2))
    Ypoint1.append(np.random.uniform(-2,2))
    Xpoint2.append(np.random.uniform(-2, 2))
    Ypoint2.append(np.random.uniform(-2,2))
    Xpoint3.append(np.random.uniform(-2, 2))
    Ypoint3.append(np.random.uniform(-2,2))
    Xpoint4.append(np.random.uniform(-2, 2))
    Ypoint4.append(np.random.uniform(-2,2))
    Xpoint5.append(np.random.uniform(-2, 2))
    Ypoint5.append(np.random.uniform(-2,2))
Xpoint1.sort()
Xpoint2.sort()
Xpoint3.sort()
Xpoint4.sort()
Xpoint5.sort()
newY1=Ypoint1.copy()
newY2=Ypoint2.copy()
newY3=Ypoint3.copy()
newY4=Ypoint4.copy()
newY5=Ypoint5.copy()
sca1=ax1.scatter(Xpoint1,newY1,5,c='red')
sca2=ax1.scatter(Xpoint2,newY2,5,c='#000000')
sca3=ax1.scatter(Xpoint3,newY3,5,c='#000000')
sca4=ax1.scatter(Xpoint4,newY4,5,c='#000000')
sca5=ax1.scatter(Xpoint5,newY5,5,c='#000000')
#x = np.linspace(0,2*np.pi,100)
#y = np.sin(x)
def init():
    data1 = [[X, Y] for X, Y in zip(Xpoint1, newY1)]
    data2 = [[X, Y] for X, Y in zip(Xpoint2, newY2)]
    data3 = [[X, Y] for X, Y in zip(Xpoint3, newY3)]
    data4 = [[X, Y] for X, Y in zip(Xpoint4, newY4)]
    data5 = [[X, Y] for X, Y in zip(Xpoint5, newY5)]
    sca1.set_offsets(data1)
    sca2.set_offsets(data2)
    sca3.set_offsets(data3)
    sca4.set_offsets(data4)
    sca5.set_offsets(data5)
    label="timestep{0}".format(0)
    ax1.set_xlabel(label)
    return sca1,sca2,sca3,sca4,sca5,ax1

def animate(i):
    size=len(Xpoint1)
    for s in range(1,size):
        newY1[s] = Ypoint1[s] + 1 * np.sin(1 * (i-s)/30)
        newY2[s] = Ypoint2[s] + 1 * np.sin(1 * (i-s)/30)
        newY3[s] = Ypoint3[s] + 1 * np.sin(1 * (i-s)/30)
        newY4[s] = Ypoint4[s] + 1 * np.sin(1 * (i-s)/30)
        newY5[s] = Ypoint5[s] + 1 * np.sin(1 * (i-s)/30)
    newX1 = Xpoint1
    newX2 = Xpoint2
    newX3 = Xpoint3
    newX4 = Xpoint4
    newX5 = Xpoint5

    data1 = [[X, Y] for X, Y in zip(newX1, newY1)]
    data2 = [[X, Y] for X, Y in zip(newX2, newY2)]
    data3 = [[X, Y] for X, Y in zip(newX3, newY3)]
    data4 = [[X, Y] for X, Y in zip(newX4, newY4)]
    data5 = [[X, Y] for X, Y in zip(newX5, newY5)]
    sca1.set_offsets(data1)
    sca2.set_offsets(data2)
    sca3.set_offsets(data3)
    sca4.set_offsets(data4)
    sca5.set_offsets(data5)
    label = "timestep{0}".format(i)
    ax1.set_xlabel(label)
    return sca1,sca2,sca3,sca4,sca5,ax1

ani = animation.FuncAnimation(fig=fig,func=animate,frames=1000,init_func=init,interval=100,blit=False)
plt.show()

