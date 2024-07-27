import cv2
cap=cv2.VideoCapture('car2.mp4')
if (cap.isOpened()== False):
    print("error")
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
