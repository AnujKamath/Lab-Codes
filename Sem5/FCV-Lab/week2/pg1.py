# # 1. Write a program to read an image and perform histogram equalization.
#
# import cv2
# import numpy as np
# img = cv2.imread('minion.jpeg',0)
# equ = cv2.equalizeHist(img)
# res = np.hstack((img, equ))
#
# # show image input vs output
# cv2.imshow('image', res)
# # cv2.imshow('Normal image',equ)
# cv2.waitKey(0)
#
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('minion.jpeg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
