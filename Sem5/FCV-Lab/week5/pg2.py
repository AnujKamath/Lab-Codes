import cv2
import numpy as np

img = cv2.imread(r"../assets/minion.png", 0)

def lbp(img, n_size=3):
    h, w = img.shape
    lbp_img = np.zeros_like(img, dtype=np.uint8)
    r = (n_size - 1) // 2
    P = n_size ** 2 - 1
    offsets = [(int(r * np.sin(2 * np.pi * p / P)), int(r * np.cos(2 * np.pi * p / P))) for p in range(P)]
    for y in range(r, h - r):
        for x in range(r, w - r):
            center = img[y, x]
            b_code = 0
            for i, (dy, dx) in enumerate(offsets):
                n_y, n_x = y + dy, x + dx
                if img[n_y, n_x] >= center:
                    b_code |= (1 << i)
            
            lbp_img[y, x] = b_code
    return lbp_img

lbp_img = lbp(img, n_size=3)

cv2.imshow('LBP Result', np.hstack((img, lbp_img)))
cv2.waitKey(0)
cv2.destroyAllWindows()
