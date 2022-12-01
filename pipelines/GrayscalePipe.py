import cv2

class GrayscalePipeline:    
    
    # Return grayscale image in uint8 format
    def process(self, image):
        output_image = np.zeros((1, 1, 1), dtype = "uint8")
        cv2.cvtColor(image, cv2.COLOR_BGR2GRAY, output_image)
        return output_image


