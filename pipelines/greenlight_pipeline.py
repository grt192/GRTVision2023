from pipelines.base_pipeline import BasePipeline


# takes in camera frames
# estimates the relative position from the camera to the target that reflects green
# outputs the relative position estimate of the green target from the camera as a tuple
# ex: (0, 1.5, 1)

class GreenLightPipeline(BasePipeline):
    def process(self, image, params, logger, ts):
        return
