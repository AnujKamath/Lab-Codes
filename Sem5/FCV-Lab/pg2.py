import cv2
import numpy as np

def lucas_kanade_optical_flow(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT_create()
    keypoints, _ = sift.detectAndCompute(old_gray, None)
    p0 = np.array([kp.pt for kp in keypoints], dtype=np.float32)

    while True:
        ret, frame = cap.read()
        if not ret: break
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        Ix = cv2.Sobel(old_gray, cv2.CV_64F, 1, 0, ksize=5)
        Iy = cv2.Sobel(old_gray, cv2.CV_64F, 0, 1, ksize=5)
        It = frame_gray.astype(np.float64) - old_gray.astype(np.float64)
        flow_vectors = []

        for point in p0:
            x, y = int(point[0]), int(point[1])
            if x < 5 or x >= old_gray.shape[1] - 5 or y < 5 or y >= old_gray.shape[0] - 5: continue
            Ix_window = Ix[y-5:y+6, x-5:x+6].flatten()
            Iy_window = Iy[y-5:y+6, x-5:x+6].flatten()
            It_window = It[y-5:y+6, x-5:x+6].flatten()
            A = np.vstack((Ix_window, Iy_window)).T
            b = -It_window
            if A.shape[0] >= 2:
                nu = np.linalg.pinv(A).dot(b)
                flow_vectors.append((x + nu[0], y + nu[1]))

        flow_vectors = np.array(flow_vectors, dtype=np.float32)
        for i, (new, old) in enumerate(zip(flow_vectors, p0)):
            a, b = new
            c, d = old
            frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 255, 0), -1)
            frame = cv2.line(frame, (int(a), int(b)), (int(c), int(d)), (255, 0, 0), 2)

        cv2.imshow('Optical Flow Tracking', frame)
        old_gray = frame_gray.copy()
        p0 = flow_vectors.reshape(-1, 1, 2)
        if cv2.waitKey(30) & 0xFF == ord('q'): break

    cap.release()
    cv2.destroyAllWindows()

def klt_tracker(video_path):
    cap = cv2.VideoCapture(video_path)
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(old_gray, maxCorners=100, qualityLevel=0.01, minDistance=10)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        p1, st, _ = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, corners, None)
        good_new = p1[st == 1]
        good_old = corners[st == 1]

        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 255, 0), -1)
            frame = cv2.line(frame, (int(a), int(b)), (int(c), int(d)), (255, 0, 0), 2)

        cv2.imshow('KLT Tracker', frame)
        old_gray = frame_gray.copy()
        corners = good_new.reshape(-1, 1, 2)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

video_path = '../assets/slow_traffic_small.mp4'
lucas_kanade_optical_flow(video_path)
# or
# klt_tracker(video_path)
