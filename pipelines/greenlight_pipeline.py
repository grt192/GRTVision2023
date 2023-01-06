from pipelines.base_pipeline import BasePipeline
from util.jetson_data import JetsonData
from multiprocessing import Process, SimpleQueue
import time

# takes in camera frames
# estimates the relative position from the camera to the target that reflects green
# outputs the relative position estimate of the green target from the camera as a tuple
# ex: (0, 1.5, 1)

class GreenLightPipeline(BasePipeline):
    def process(self, image, params, ts):


        pos = (0,0,0) #STUB
        rot = (0,0,0) #STUB

        data = JetsonData(
            translation=pos,
            rotation=rot,
            ts=int(time.time() * 1000),
            tid=16,
            cid=3
        )
        self.data_queue.put(data)
        return

