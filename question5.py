import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', size=8)          # controls default text sizes
plt.rc('axes', titlesize=16)    # fontsize of the axes title
plt.rc('axes', labelsize=16)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=8)    # fontsize of the tick labels
plt.rc('ytick', labelsize=8)    # fontsize of the tick labels
plt.rc('legend', fontsize=14)    # legend fontsize
plt.rc('figure', titlesize=20)  # fontsize of the figure title

i_bar = 1

i_bar0 = 1
i_bar1 = 2

i = np.arange(0, 10, 0.1)
z = np.arange(0, 10, 0.1)

# fx = np.exp(-i * i_bar) * i_bar
# fy = np.exp(-i *i_bar) * i_bar
# fz = np.exp(-z *i_bar) * z * i_bar**2

fx = np.exp(-i * i_bar0) * i_bar0
fy = np.exp(-i * i_bar1) * i_bar1
fz = (i_bar0 * i_bar1)/(i_bar1 - i_bar0)*(np.exp(-i * i_bar0)-np.exp(-i * i_bar1))

plt.figure(figsize=(10, 8))
plt.plot(i, fx, label="fx")
plt.plot(i, fy, label="fy")
plt.plot(z, fz, label="fz")

plt.legend()
plt.show()
