import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import camera.camera_source as camera_source

# hacky way to just use the same logic already in CameraSource
class TestCameraSource(camera_source):
    pass