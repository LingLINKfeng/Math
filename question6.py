import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft2
import math

import skimage.io as io

img=np.zeros((256,256))
for i in range(0,256):
    for j in range(0,256):
        if(i>120 and i<130 and j>120 and j<130):
            img[i][j]=255

def FFT_SHIFT(img):
    m,n = img.shape
    for i in range(0,m):
        for j in range(0,n):
            img[i][j] = img[i][j] * math.pow(-1,(i+j))
            #img[i,j] = img[i,j]*(-1)**(i+j)
    return img

# img=io.imread("squre.jpg")
# img=img[:,:,1]

img=FFT_SHIFT(img)
img=fft2(img)

plt.imshow(np.abs(img), cmap='gray')
plt.show()