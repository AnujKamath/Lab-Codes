import cv2
image = cv2.imread('minion.jpeg')

start_point = (50, 5)
end_point = (200, 140)
color = (255, 0, 0)
thickness = 2

image = cv2.rectangle(image, start_point, end_point, color, thickness)

# Displaying the image
cv2.imshow('Image with Rectangle', image)
cv2.waitKey(0)

