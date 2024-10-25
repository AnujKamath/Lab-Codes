import cv2
import numpy as np

img1 = cv2.imread('box.png')
img2 = cv2.imread('box_in_scene.png')

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


def stitch(img1, img2):
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    matcher = cv2.BFMatcher()
    all_matches = matcher.knnMatch(des1, des2, k=2)

    good = [m for m, n in all_matches if m.distance < 0.75 * n.distance]

    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    H = homography(src_pts, dst_pts)

    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    c_img1 = np.float32([[0, 0], [0, h1], [w1, 0], [w1, h1]]).reshape(-1, 1, 2)
    c_img2 = np.float32([[0, 0], [0, h2], [w2, 0], [w2, h2]]).reshape(-1, 1, 2)
    tc_img2 = cv2.perspectiveTransform(c_img2, H)

    all_corners = np.concatenate((c_img1, tc_img2), axis=0)
    [x_min, y_min] = all_corners.min(axis=0).astype(np.int32).flatten()
    [x_max, y_max] = all_corners.max(axis=0).astype(np.int32).flatten()

    off = [-x_min, -y_min]
    H_offset = np.array([[1, 0, off[0]], [0, 1, off[1]], [0, 0, 1]])

    stitched = cv2.warpPerspective(img2, H_offset @ H, (x_max - x_min, y_max - y_min))
    stitched[off[1]:h1 + off[1], off[0]:w1 + off[0]] = img1

    return stitched


output = stitch(img1, img2)
cv2.imshow('Output', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
