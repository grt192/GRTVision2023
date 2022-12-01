import cv2

class DrawTagsPipe:    
    
    # Return grayscale image in uint8 format
    def process(self, image, detections):
        output_image = cv2.copy(image)

        for d in detections:
            # Extract bounding box coordinates
            (ptA, ptB, ptC, ptD) = d.corners
            ptB = (int(ptB[0]), int(ptB[1]))
            ptC = (int(ptC[0]), int(ptC[1]))
            ptD = (int(ptD[0]), int(ptD[1]))
            ptA = (int(ptA[0]), int(ptA[1]))

            # Draw bounding box
            cv2.line(output_image, ptA, ptB, (0, 255, 0), 2)
            cv2.line(output_image, ptB, ptC, (0, 255, 0), 2)
            cv2.line(output_image, ptC, ptD, (0, 255, 0), 2)
            cv2.line(output_image, ptD, ptA, (0, 255, 0), 2)
            
            # Draw center of tag
            (cX, cY) = (int(d.center[0]), int(d.center[1]))
            cv2.circle(output_image, (cX, cY), 5, (0, 0, 255), -1)
            
            # Draw the tag family on the image
            cv2.putText(output_image, str(d.tag_family, 'id' + str(d.tag_id)), 
                (ptA[0], ptA[1] - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return output_image


