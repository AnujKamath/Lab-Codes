import cv2
import numpy as np

ref = cv2.imread('box.png', 0)
scn = cv2.imread('box_in_scene.png', 0)

def display(img, height=360):
    scale = height / img.shape[0]
    width = int(img.shape[1] * scale)
    resized_img = cv2.resize(img, (width, height))
    cv2.imshow('Matches', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


sift_detect = cv2.SIFT_create()

kp_ref, des_ref = sift_detect.detectAndCompute(ref, None)
kp_scn, des_scn = sift_detect.detectAndCompute(scn, None)

matcher = cv2.BFMatcher()
all_matches = matcher.knnMatch(des_ref, des_scn, k=2)

filtered_matches = []
for m1, m2 in all_matches:
    if m1.distance < 0.75 * m2.distance:
        filtered_matches.append([m1])

result_img = cv2.drawMatchesKnn(ref, kp_ref, scn, kp_scn, filtered_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
display(result_img)
