import cv2
import numpy as np
i=0
cap=cv2.VideoCapture("LicPlateImages/projecttest.mp4")
while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    print cap.isOpened(),i
    i=i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release
cv2.destroyAllWindows()
