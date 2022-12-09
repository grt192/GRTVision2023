import cv2
import numpy as np


class GrayscalePipe:
    # Return grayscale image in uint8 format
    def process(self, image):
        output_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return output_image
