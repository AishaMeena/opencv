import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, img = cap.read()
    circle= cv2.circle(img, [0,112],1,[255,0,0])
    pt1=  np.float32([[0,0],[0,112],[0,113],[0,140]])
    pt2 = np.float32([[0, 0], [0, 112], [0, 113], [0, 140]])

    matrix= cv2.getPerspectiveTransform(pt1,pt2)
    result=cv2.warpPerspective(img,matrix,(500,600))

    cv2.imshow('frame', img)
    cv2.imshow('frame1', result)
    img = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img,(3,3))
    _,thrash = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    for contour in contours:
        


    
    
    

    if cv2.waitKey(1)==27:
        break


cap.release()
cv2.destroyAllWindows()