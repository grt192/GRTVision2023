import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import camera.CameraSource as CameraSource

# hacky way to just use the same logic already in CameraSource
class TestCameraSource(CameraSource):
    pass