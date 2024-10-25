import cv2
import numpy as np

img = cv2.imread("../assets/minion.png", 0)

CELL, BIN, STRD, BLK = 8, 9, 2, 2
gx = cv2.filter2D(img, ddepth=-1, kernel=np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]))
gy = cv2.filter2D(img, ddepth=-1, kernel=np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]]))

mag, angle = np.sqrt(gx**2 + gy**2), (np.arctan2(gy, gx) * 180.0 / np.pi) % 180

def hist(mag, angle):
    h = np.zeros(BIN)
    b_w = 180 / BIN
    for y in range(mag.shape[0]):
        for x in range(mag.shape[1]):
            a, w = angle[y, x], mag[y, x]
            b = int(a // b_w)
            n_b = (b + 1) % BIN
            r = (a % b_w) / b_w
            h[b] += w * (1 - r)
            h[n_b] += w * r
    return h

h, w = img.shape
c_y, c_x = h // CELL, w // CELL
cell_hists = np.zeros((c_y, c_x, BIN))

for y in range(c_y):
    for x in range(c_x):
        c_mag = mag[y*CELL:(y+1)*CELL, x*CELL:(x+1)*CELL]
        c_angle = angle[y*CELL:(y+1)*CELL, x*CELL:(x+1)*CELL]
        cell_hists[y, x] = hist(c_mag, c_angle)

b_y, b_x = c_y - BLK + 1, c_x - BLK + 1
hog_feats = []

for y in range(b_y):
    for x in range(b_x):
        block = cell_hists[y:y+BLK, x:x+BLK].flatten()
        hog_feats.extend(block / (np.sqrt(np.sum(block**2) + 1e-6)))

def slide_win(img, win_size, step):
    h, w = img.shape
    for y in range(0, h - win_size[1] + 1, step):
        for x in range(0, w - win_size[0] + 1, step):
            yield (x, y, img[y:y + win_size[1], x:x + win_size[0]])

win_size = (64, 128)
for (x, y, win) in slide_win(img, win_size, STRD):
    if win.shape == win_size:
        feats = np.array(hog_feats)
        print("Window:", (x, y), "Features length:", len(feats))
