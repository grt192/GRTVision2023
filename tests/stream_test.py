import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import cv2
print(cv2.getBuildInformation())

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    if cap.isOpened() is not True:
        print('what?')
        quit()

    out = cv2.VideoWriter("appsrc ! videoconvert ! videoscale ! video/x-raw,format=I420,width=1080,height=240,framerate=5/1 !  videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! port=5000")

    while True:
        _, frame = cap.read()
        out.write(frame)

