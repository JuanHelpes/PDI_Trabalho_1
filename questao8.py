import numpy as np
import cv2
from matplotlib import pyplot as plt

#carrega o video
cap = cv2.VideoCapture('VideoQ8L.mp4')

for i in range(1, int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    _, frame = cap.read()
    
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #definindo o intervalo de cor que sera detectada (no caso a cor laranja)
    lowerOrange = np.array([10, 127, 0])
    upperOrange = np.array([30, 255, 255])

    mask = cv2.inRange(hsvFrame, lowerOrange, upperOrange)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if(contours):
        i=0

        maxArea = cv2.contourArea(contours[0])
        idContourMaxArea = 0
        for cnt in contours:
            if maxArea < cv2.contourArea(cnt):
                maxArea = cv2.contourArea(cnt)
                idContourMaxArea = i
            i +=1 

        x, y, w, h = cv2.boundingRect(contours[idContourMaxArea])

        if(maxArea > 100.0):
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)

        cv2.imshow('frame', frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
