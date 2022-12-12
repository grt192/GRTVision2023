import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import cv2
# print(cv2.getBuildInformation())

if __name__ == '__main__':
    cap = cv2.VideoCapture(0, )

    if cap.isOpened() is not True:
        print('what?')
        quit()

    width  = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)   # float `width`
    height = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)  # float `height`

    gstream = "appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtph264pay ! udpsink port=5000"

    out = cv2.VideoWriter(gstream, 0, 30, (width, height), True)

    while True:
        _, frame = cap.read()
        out.write(frame)

