import AprilTags
import GreenLight
import Localization
import Source

# takes in camera inputs
# sends them to Greenlight and AprilTags
# takes outputs of pipelines and sends them to Localization function
# sends the outputs back to the roborio


class Main:
    def __init__(self):
        self.green = GreenLight()
        self.localizer = Localization()

        # example source
        self.turretcam = Source(0,    0, 0 ,1,   0, 0, 0)
        # port 0
        # raised by 1 unit (feet probably?)
        # pointed straight forward
        
    
    def run(self):
        turretprediction = self.green.detect(self.turretcam.get_frame())
        location = self.localizer([turretprediction, self.turretcam])
        return location