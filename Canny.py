import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('dancing-spider.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

#canny
img_canny = cv2.Canny(img, 100, 200, 3, L2gradient=True)

plt.imshow(img)
plt.title('Original')
plt.show()
plt.imshow(img_canny)
plt.title('Canny')
plt.imsave('dancing-spider-canny.png', img_canny, cmap='gray', format='png')
plt.show()
