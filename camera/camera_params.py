import json
import math
from pathlib import Path


class CameraParams:
    """
    Config parameters for a `CameraSource`. `filename` should be a path to a camera config JSON file.
    """
    def __init__(self, filename: str):
        print(str(Path(__file__).parent))

        file = open(str(Path(__file__).parent) + '/config/' + filename + '.json')
        data = json.load(file)

        self.path = data['path']
        self.name = data['name']
        self.res_width = data['res_width']
        self.res_height = data['res_height']
        self.fps = data['fps']

        self.distortion = data['cam_calib']['distortion']
        self.cam_matrix = data['cam_calib']['cam_matrix']
        self.rvecs = data['cam_calib']['rvecs']
        self.tvecs = data['cam_calib']['tvecs']

        self.FOV = data['FOV']

        # Calculate horz/vert FOV by similar triangles
        hypot_pixels = math.hypot(self.res_width, self.res_height)
        self.FOV_horz = self.FOV * self.res_width / hypot_pixels
        self.FOV_vert = self.FOV * self.res_height / hypot_pixels

        print("Read camera config for", self.name, "at", self.path)
        print(data)

    # Return (fx, fy, cx, cy) 
    def get_params_april(self):
        return self.cam_matrix[0][0], self.cam_matrix[1][1], self.cam_matrix[0][2], self.cam_matrix[1][2]
