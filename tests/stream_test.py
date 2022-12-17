import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import cv2
# print(cv2.getBuildInformation())

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    if cap.isOpened() is not True:
        print('what?')
        quit()

    width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`

    print(str(width) + " " + str(height))

    gstream = "appsrc ! videoconvert ! videoscale ! video/x-raw,width=640,height=480, framerate=30/1 ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! udpsink port=49999 host=192.168.55.100" 

    out = cv2.VideoWriter(gstream, 0, 30.0, (int(width), int(height)))

    while True:
        _, frame = cap.read()
        cv2.rectangle(frame, (10,10), (100,100), (255,0,0), 2)
        out.write(frame)

