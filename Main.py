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
        self.data = dict()

        self.pipelines = [self.green, self.localizer]

        # example source
        self.turretcam = Source(0,    0, 0 , 1,   0, 0, 0)
        # port 0
        # raised by 1 unit (feet probably?)
        # pointed straight forward

        self.sources = [self.turretcam]
        
    
    def run(self):
        
        data = dict()

        for i in range(len(self.sources)):
            data[self.sources[i]] = dict()
            img = self.sources[i].get_frame()
            for pipeline in self.pipelines:
                data[self.sources[i]][pipeline] = (pipeline.get(img))
        
        greenlights = []
        apriltags = []

        for source in data:
            greenlights.append((source, data[source][self.green]))
            apriltags.append((source, data[source][self.april]))



        location = self.localizer.localize(greenlights, apriltags)
        return location