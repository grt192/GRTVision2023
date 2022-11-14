# retrieves frames from a single camera, stores that camera's position as well

import cv2

class Source:

    def __init__(self, port, x, y, z, a, b, c):
        self.port = port
        self.cap = None
        self.frame = None

        # relative position and angle to robot origin
        self.pos = (x, y, z)
        self.angle = (a, b, c)
    
    def get_frame(self):

        if self.cap is None or (not self.cap.isOpened()):
            self.cap = cv2.VideoCapture(self.port)

        self.frame = self.cap.read()