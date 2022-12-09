import cv2


def grayscale_pipe(image):
    """
    Pipe that processes an image into grayscale `uint8` format.
    """
    output_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return output_image
