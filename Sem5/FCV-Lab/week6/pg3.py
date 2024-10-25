import cv2
import numpy as np

ref = cv2.imread('box.png', 0)
scn = cv2.imread('box_in_scene.png', 0)

def display(img, h=360):
    scale = h / img.shape[0]
    w = int(img.shape[1] * scale)
    resized = cv2.resize(img, (w,h))
    cv2.imshow('Output', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def homography(src_pts, dst_pts):
    m = []
    for i in range(len(src_pts)):
        x, y = src_pts[i][0]
        u, v = dst_pts[i][0]
        m.append([-x, -y, -1, 0, 0, 0, x * u, y * u, u])
        m.append([0, 0, 0, -x, -y, -1, x * v, y * v, v])
    
    m = np.array(m)
    _, _, vh = np.linalg.svd(m)
    H = vh[-1].reshape(3, 3)
    return H / H[2, 2]


sift = cv2.SIFT_create()
kp_ref, des_ref = sift.detectAndCompute(ref, None)
kp_scn, des_scn = sift.detectAndCompute(scn, None)

matcher = cv2.BFMatcher()
all_matches = matcher.knnMatch(des_ref, des_scn, k=2)

matches = []
for first, second in all_matches:
    if first.distance < 0.75 * second.distance:
        matches.append(first)

src_pts = np.float32([kp_ref[match.queryIdx].pt for match in matches]).reshape(-1, 1, 2)
dst_pts = np.float32([kp_scn[match.trainIdx].pt for match in matches]).reshape(-1, 1, 2)

h_matrix = homography(src_pts, dst_pts)

mask = [1] * len(matches)
draw_set = dict(matchColor=(0, 255, 0), singlePointColor=(255, 0, 0), matchesMask=mask, flags=0)
output = cv2.drawMatchesKnn(ref, kp_ref, scn, kp_scn, [[m] for m in matches], None, **draw_set)

display(output)
