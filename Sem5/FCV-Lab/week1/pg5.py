import cv2
img = cv2.imread('minion.jpeg')
img = cv2.resize(img,(500,500))
cv2.imshow('Normal image',img)
cv2.waitKey(0)
