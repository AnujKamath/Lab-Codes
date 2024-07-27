import cv2
img = cv2.imread('minion.jpeg')
gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_minion.jpeg',gray_image)
cv2.imshow('Normal image',img)
cv2.imshow('gray image',gray_image)
cv2.waitKey(0)

