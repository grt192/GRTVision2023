import cv2


class GrayscalePipe:
    """
    Pipe that processes an image into grayscale `uint8` format.
    """
    def process(self, image):
        output_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return output_image
