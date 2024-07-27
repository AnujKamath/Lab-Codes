import cv2
img = cv2.imread('minion.jpeg')
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Normal image',img)
cv2.waitKey(0)
