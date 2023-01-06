import numpy as np
import cv2 as cv
import math
import platform

def nothing(x):
    pass

system = platform.platform()

# create trackbar windows
cv.namedWindow('Hue', cv.WINDOW_NORMAL)
cv.namedWindow('Saturation', cv.WINDOW_NORMAL)
cv.namedWindow('Value', cv.WINDOW_NORMAL)

# resize trackbar windows
cv.resizeWindow('Hue', 1250, 30)
cv.resizeWindow('Saturation', 1250, 30)
cv.resizeWindow('Value', 1250, 30)

# create trackbars
cv.createTrackbar('low_H', 'Hue', 0, 255, nothing)
cv.createTrackbar('high_H', 'Hue', 0, 255, nothing)

cv.createTrackbar('low_S', 'Saturation', 0, 255, nothing)
cv.createTrackbar('high_S', 'Saturation', 0, 255, nothing)

cv.createTrackbar('low_V', 'Value', 0, 255, nothing)
cv.createTrackbar('high_V', 'Value', 0, 255, nothing)

# set trackbar number for hue max and mins
cv.setTrackbarPos('high_H', 'Hue', 95)
cv.setTrackbarPos('low_H', 'Hue', 25)
# set trackbar number for saturation max and mins
cv.setTrackbarPos('high_S', 'Saturation', 255)
cv.setTrackbarPos('low_S', 'Saturation', 80)
# set trackbar number for value max and mins
cv.setTrackbarPos('high_V', 'Value', 255)
cv.setTrackbarPos('low_V', 'Value', 80)

camangle = 0

#capture video
if "Ubuntu" in system:
    capture = cv.VideoCapture(0, cv.CAP_V4L2)
else:
    capture = cv.VideoCapture(1)

# if camera couldn't be opened, exit
if not capture.isOpened():
    print("Can't open camera")
    exit()

while True:
    #capture vid frame by frame
    ret, frame = capture.read()
    if "Ubuntu" in system:
        capture.set(cv.CAP_PROP_AUTO_EXPOSURE, 1)
        capture.set(cv.CAP_PROP_EXPOSURE, 10)
    else:
        capture.set(cv.CAP_PROP_EXPOSURE, -15)

    contour_img = np.copy(frame)

    # if frame is not read correctly, break
    if not ret:
        print("Can't get frame")
        break

    # frame RGB to HSV
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowH = cv.getTrackbarPos('low_H', 'Hue')
    highH = cv.getTrackbarPos('high_H', 'Hue')
    # assign trackbar position to min max saturation
    lowS = cv.getTrackbarPos('low_S', 'Saturation')
    highS = cv.getTrackbarPos('high_S', 'Saturation')
    # assign trackbar position to min max value
    lowV = cv.getTrackbarPos('low_V', 'Value')
    highV = cv.getTrackbarPos('high_V', 'Value')

    # frame HSV to binary og (45, 100, 100) (105, 255, 255)
    binary_frame = cv.inRange(hsv_frame, (lowH, lowS, lowV), (highH, highS, highV))

    # find contours of binary img
    contour_list, hierarchy = cv.findContours(binary_frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if len(contour_list) > 0:
        largest = contour_list[0]
        height, width, _ = contour_img.shape
        min_x, min_y = width, height
        print(min_x)
        max_x =  max_y = 0
        #find minimum area rectangle
        for contours in contour_list:            
            if cv.contourArea(contours) < 25:
                continue
            if cv.contourArea(contours) > cv.contourArea(largest):
                largest = contours
            #get NON-ROTATING rectangle
            x, y, w, h = cv.boundingRect(contours)
            min_x, max_x = min( x, min_x), max(x+w , max_x)
            min_y, max_y = min( y, min_y), max(y+h, max_y)
            cv.drawContours(contour_img, contours, -1, color = (255, 255, 255), thickness = 1 )
            cv.rectangle(contour_img,(x,y),(x+w,y+h),(0, 255, 0), 2)
        #print encompassing rectangle
        cv.rectangle(contour_img, (min_x, min_y), (max_x, max_y), (255, 0, 0), 2)
        #this still uses rotatabled rectangle as of now
        largerect = cv.minAreaRect(largest)
        small = largerect[1][1]
        large = largerect[1][0]

        if(largerect[1][0] < small):
            small = largerect[1][0]
            large = largerect[1][1]
        # print((small))
        #get ratio of sides, print
        if(small != 0):
            ratio = (large/small)
            if(ratio < 1.88):
                # print(ratio)

                frameAngle = ((max_x + min_x) / 2 - 320) / 640 * 57.15 #alpha in figure

                distance = math.acos(ratio/1.88) * 180 / (math.pi) #d in figure

                rotatedAngle =  2.125 * 700 *math.cos(camangle) / small #theta in figure

                relativeRotation = rotatedAngle - frameAngle #phi in figure

                xdist = distance * math.sin(frameAngle / 360 * (2 * math.pi)) * 360 #in degrees
                ydist = distance * math.cos(frameAngle / 360 * (2 * math.pi)) * 360 #in degrees

                pos = (x, y, 0) #z is ignored since it doesn't change
                rot = (0, 0, relativeRotation) #x and y rotations are ignored since they don't change


        # print((largerect[1][1] * 24) / 2.06)
        # if(largerect[1][1] != 0):
        #     print (2.06 * 700 / small)

    # display frame
    cv.imshow('contour_frame', contour_img)

    # if q (quit) pressed, break
    if cv.waitKey(1) == ord('q'):
        break

    # if r pressed, reset trackbars
    if cv.waitKey(1) == ord('r'):
        # set trackbar number for saturation max and mins
        cv.setTrackbarPos('high_H', 'Hue', 95)
        cv.setTrackbarPos('low_H', 'Hue', 25)
        # set trackbar number for saturation max and mins
        cv.setTrackbarPos('high_S', 'Saturation', 255)
        cv.setTrackbarPos('low_S', 'Saturation', 80)
        # set trackbar number for value max and mins
        cv.setTrackbarPos('high_V', 'Value', 255)
        cv.setTrackbarPos('low_V', 'Value', 80)

capture.release()
cv.destroyAllWindows()
