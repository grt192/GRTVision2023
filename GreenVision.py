import numpy as np
import cv2 as cv

def nothing(x):
    pass

#create trackbar windows
cv.namedWindow('Hue', cv.WINDOW_NORMAL)
cv.namedWindow('Saturation', cv.WINDOW_NORMAL)
cv.namedWindow('Value', cv.WINDOW_NORMAL)

#resize trackbar windows
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


#set trackbar number for hue max and mins
cv.setTrackbarPos('high_H', 'Hue', 95)
cv.setTrackbarPos('low_H', 'Hue', 25)
#set trackbar number for saturation max and mins
cv.setTrackbarPos('high_S', 'Saturation', 255)
cv.setTrackbarPos('low_S', 'Saturation', 80)
#set trackbar number for value max and mins
cv.setTrackbarPos('high_V', 'Value', 255)
cv.setTrackbarPos('low_V', 'Value', 80)


#capture video
capture = cv.VideoCapture(0)

#if camera couldn't be opened, exit
if not capture.isOpened():
    print("Can't open camera")
    exit()

while True:
    #capture vid frame by frame
    ret, frame = capture.read()

    contour_img = np.copy(frame)

    #if frame is not read correctly, break
    if not ret:
        print ("Can't get frame")
        break

    #frame RGB to HSV
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lowH = cv.getTrackbarPos('low_H', 'Hue')
    highH = cv.getTrackbarPos('high_H', 'Hue')
    #assign trackbar position to min max saturation
    lowS = cv.getTrackbarPos('low_S', 'Saturation')
    highS = cv.getTrackbarPos('high_S', 'Saturation')
    #assign trackbar position to min max value
    lowV = cv.getTrackbarPos('low_V', 'Value')
    highV = cv.getTrackbarPos('high_V', 'Value')

    #frame HSV to binary og (45, 100, 100) (105, 255, 255)
    binary_frame = cv.inRange(hsv_frame, (lowH, lowS, lowV), (highH, highS, highV))

    #find contours of binary img
    contour_list, hierarchy = cv.findContours(binary_frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    if len(contour_list) > 0:
        largest = contour_list[0]
        for contour in contour_list:
            if cv.contourArea(contour) > cv.contourArea(largest):
                largest = contour
            #draw contours
    #find minimum area rectangle
    rect = cv.minAreaRect(largest)
    #find 4 corners of rectangle
    box = cv.boxPoints(rect)
    #convert to int
    box = np.int0(box)
    #draw contour
    cv.drawContours(contour_img, [box], 0, color = (0, 0, 255), thickness = 2 )
    #draw rectangle around contour
    cv.drawContours(contour_img, largest, -1, color = (255, 255, 255), thickness = -3 )

    

    #display frame
    cv.imshow('contour_frame', contour_img)

    # if q (quit) pressed, break
    if cv.waitKey(1) == ord('q'):
        break

    #if r pressed, reset trackbars
    if cv.waitKey(1) == ord('r'):
        #set trackbar number for saturation max and mins
        cv.setTrackbarPos('high_H', 'Hue', 95)
        cv.setTrackbarPos('low_H', 'Hue', 25)
        #set trackbar number for saturation max and mins
        cv.setTrackbarPos('high_S', 'Saturation', 255)
        cv.setTrackbarPos('low_S', 'Saturation', 80)
        #set trackbar number for value max and mins
        cv.setTrackbarPos('high_V', 'Value', 255)
        cv.setTrackbarPos('low_V', 'Value', 80)

capture.release()
cv.destroyAllWindows()


