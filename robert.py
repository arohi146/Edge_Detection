import sys
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import io

plt.rcParams['figure.figsize'] = [15, 10]
roberts_cross_v = np.array( [[ 0, 0, 0 ],
                             [ 0, 1, 0 ],
                             [ 0, 0,-1 ]] )

roberts_cross_h = np.array( [[ 0, 0, 0 ],
                             [ 0, 0, 1 ],
                             [ 0,-1, 0 ]] )
img = io.imread('dancing-spider.jpg')
img1 = img.astype('float64')
gray_img = np.dot(img1[...,:3], [0.2989, 0.5870, 0.1140])
gray_img /= 255
vertical = ndimage.convolve( gray_img, roberts_cross_v )
horizontal = ndimage.convolve( gray_img, roberts_cross_h )
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
plt.title('dancing-spider')
plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()
plt.title('Roberts' )
plt.imshow(edged_img, cmap=plt.get_cmap('gray'))
plt.imsave('dancing-spider-robert.png', edged_img, cmap='gray', format='png')
plt.show()
