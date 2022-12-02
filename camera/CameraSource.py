# CameraSource.py
# Retrieves images from USB camera according to specified config file.

import cv2
from .CameraParams import CameraParams

class CameraSource:

    def __init__(self, filename):
        # Initialize objects
        self.cap = None
        self.frame = None

        # READ CONFIG FILE
        self.params = CameraParams(filename)
        
    
    def get_frame(self):

        # Grab frame
        if self.cap is None or (not self.cap.isOpened()):
            self.cap = cv2.VideoCapture(self.params.path) # , cv2.CAP_V4L)
            
        _, self.frame = self.cap.read()

        # CALIBRATE IMAGE PIPE

        # RESIZE IMAGE PIPE

        return self.frame # TODO fix