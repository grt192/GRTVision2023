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
        self.april = AprilTags()
        self.localizer = Localization()

        self.pipelines = [self.green, self.localizer]

        # example source
        self.turretcam = Source(0,    0, 0 ,1,   0, 0, 0)
        # port 0
        # raised by 1 unit (feet probably?)
        # pointed straight forward

        self.sources = [self.turretcam]
        
    
    def run(self):
        
        greenlights = []
        apriltags = []

        for source in self.sources:
            img = source.get_frame()
            greenlights.append((source, self.green.get(img)))
            apriltags.append((source, self.april.get(img)))
            


        location = self.localizer.localize(greenlights, apriltags)
        return location