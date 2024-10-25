import cv2
import numpy as np

img = cv2.imread("image_resized.png", 0)
print(img)

def comp_grad(img):
    kx = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]])
    ky = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]])
    
    gx = cv2.filter2D(img, -1, kx)
    gy = cv2.filter2D(img, -1, ky)
    return gx, gy

LEVELS = 5
gauss_pyramid = []
temp = img.copy()
for i in range(1, LEVELS):
    temp = cv2.GaussianBlur(temp, (5,5), 0)
    temp = cv2.resize(temp, (temp.shape[1]//2 , temp.shape[0]//2))
    gauss_pyramid.append(temp)
dog_pyramid = []
for i in range(1, LEVELS):
    dog_pyramid.append(cv2.subtract(gauss_pyramid[i - 1], gauss_pyramid[i]))

THRESH = 0.03
keyp = []
for i, dog in enumerate(dog_pyramid):
    for y in range(1, dog.shape[0] - 1):
        for x in range(1, dog.shape[1] - 1):
            patch = dog[y - 1:y + 2, x - 1:x + 2]
            if (np.abs(dog[y, x]) > THRESH and (np.all(dog[y, x] >= patch) or np.all(dog[y, x] <= patch))):
                keyp.append((x, y, i))

orients = []
for x, y, level in keyp:
    gx, gy = comp_grad(img)
    mag = np.sqrt(gx**2 + gy**2)
    dir = np.arctan2(gy[y, x], gx[y, x]) * (180 / np.pi) % 360
    orients.append((x, y, level, dir))

desc = []
for x, y, level, orient in orients:
    patch = gauss_pyramid[level][y - 8:y + 8, x - 8:x + 8]
    patch = cv2.resize(patch, (16, 16)).flatten()
    desc.append(patch)


desc = np.array(desc)
print(desc)