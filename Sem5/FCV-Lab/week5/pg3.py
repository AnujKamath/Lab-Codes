import cv2
import numpy as np

img = cv2.imread(r"minions.jpeg", 0)

C_SZ = 8
BNS = 9
STP = 2
BLK_SZ = 2

kx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])

ky = np.array([[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]])

dx = cv2.filter2D(img, ddepth=-1, kernel=kx)
dy = cv2.filter2D(img, ddepth=-1, kernel=ky)

mag = np.sqrt(dx**2 + dy**2)
ang = (np.arctan2(dy, dx) * 180.0 / np.pi) % 180

def hist_comp(mag, ang):
    hist = np.zeros(BNS)
    b_wid = 180 / BNS
    for j in range(mag.shape[0]):
        for i in range(mag.shape[1]):
            a = ang[j, i]
            b = int(a // b_wid)
            w = mag[j, i]
            nxt_b = (b + 1) % BNS
            r = (a % b_wid) / b_wid
            hist[b] += w * (1 - r)
            hist[nxt_b] += w * r
    return hist

h, w = img.shape
cy = h // C_SZ
cx = w // C_SZ
cell_hists = np.zeros((cy, cx, BNS))

for j in range(cy):
    for i in range(cx):
        cell_mag = mag[j * C_SZ:(j + 1) * C_SZ, i * C_SZ:(i + 1) * C_SZ]
        cell_ang = ang[j * C_SZ:(j + 1) * C_SZ, i * C_SZ:(i + 1) * C_SZ]
        cell_hists[j, i] = hist_comp(cell_mag, cell_ang)

by = cy - BLK_SZ + 1
bx = cx - BLK_SZ + 1
features = []

for j in range(by):
    for i in range(bx):
        blk = cell_hists[j:j + BLK_SZ, i:i + BLK_SZ].flatten()
        norm = np.sqrt(np.sum(blk**2) + 1e-6)
        features.extend(blk / norm)

def slide_win(img, win_sz, step):
    h, w = img.shape
    for j in range(0, h - win_sz[1] + 1, step):
        for i in range(0, w - win_sz[0] + 1, step):
            yield (i, j, img[j:j + win_sz[1], i:i + win_sz[0]])

win_sz = (64, 128)
for (i, j, win) in slide_win(img, win_sz, STP):
    if win.shape[0] == win_sz[1] and win.shape[1] == win_sz[0]:
        feat_vec = np.array(features)
        print("Pos:", (i, j), "Feature len:", len(feat_vec))
