import cv2
import numpy as np
cap = cv2.VideoCapture(0)

for i in range(10):
    ret, frame1 = cap.read()
frame1 = np.flip(frame1, axis=1)
l_b = np.array([76, 46, 40])
u_b = np.array([107, 255, 255])

while (cap.isOpened()):
    ret, img = cap.read()
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, l_b, u_b)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    img[np.where(mask == 255)] = frame1[np.where(mask == 255)]
    cv2.imshow('IC', img)

    k = cv2.waitKey(1)
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()