import cv2
import numpy as np

img_a = cv2.imread('image1.png', 0)
img_b = cv2.imread('image2.png', 0)

def pairwise_dist(set_a, set_b):
    return np.linalg.norm(set_a[:, np.newaxis] - set_b[np.newaxis, :], axis=2)

def find_nearest(set_a, set_b, k=1):
    dist = pairwise_dist(set_a, set_b)
    idx_nearest = np.argsort(dist, axis=1)[:, :k]
    dist_nearest = np.take_along_axis(dist, idx_nearest, axis=1)
    return idx_nearest, dist_nearest


detector = cv2.SIFT_create()
kp_a, desc_a = detector.detectAndCompute(img_a, None)
kp_b, desc_b = detector.detectAndCompute(img_b, None)

if desc_a is not None and desc_b is not None:
    match_idxs, match_dists = find_nearest(desc_a, desc_b, k=1)
    for i, (m_idx, m_dist) in enumerate(zip(match_idxs, match_dists)):
        print(f"Desc {i} matches with {m_idx[0]} at dist {m_dist[0]:.2f}")

    matched_img = cv2.drawMatches(img_a, kp_a, img_b, kp_b, 
                                  [cv2.DMatch(i, m_idx[0], m_dist[0]) for i, m_idx, m_dist in zip(range(len(match_idxs)), match_idxs, match_dists)], 
                                  None, 
                                  flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    cv2.imshow('Matches', matched_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
