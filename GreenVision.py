import numpy as np
import cv2 as cv

def nothing(x):
    pass

cv.namedWindow('binary_frame')

#hue max and min trackbars
cv.createTrackbar('high_H', 'binary_frame', 0, 255, nothing)
#cv.createTrackbar('low_H', 'binary_frame', 0, 255, nothing)

#cv.setTrackbarPos('low_H', 'binary_frame', 45)
#cv.setTrackbarPos('high_H', 'binary_frame', 105)

#capture video
capture = cv.VideoCapture(0)

#if camera couldn't be opened,exit
if not capture.isOpened():
    print("Can't open camera")
    exit()

while True:
    #capture vid frame by frame
    ret, frame = capture.read()

    #if frame is not read correctly, break
    if not ret:
        print ("Can't get frame")
        break

    #assign trackbar position to min max hue
    #lowH = cv.getTrackbarPos('low_H', 'binary_frame')
    highH = cv.getTrackbarPos('high_H', 'binary_frame')

    #frame RGB to HSV
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    #frame HSV to binary og (45, 100, 100) (105, 255, 255)
    binary_frame = cv.inRange(hsv_frame, (45, 100, 100), (105, 255, 255))

    #display frame
    cv.imshow('binary_frame', binary_frame)
    cv.imshow('frame', frame)


    # if q (quit) pressed, break
    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()


