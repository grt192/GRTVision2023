# Reads and stores camera config file (json).

import json 
import math
from pathlib import Path


class CameraParams:
    def __init__(self, filename):

        print(str(Path(__file__).parent))
        
        file = open(str(Path(__file__).parent) + '/config/'+ filename + '.json')
        data = json.load(file)

        self.path = data['path']
        self.name = data['name']
        self.res_width = data['res_width']
        self.res_height = data['res_height']
        
        self.distortion = data['cam_calib']['distortion']
        self.cam_matrix = data['cam_calib']['cam_matrix']
        self.rvecs = data['cam_calib']['rvecs']
        self.tvecs = data['cam_calib']['tvecs']

        self.FOV = data['FOV']
        
        # Calculate horz/vert FOV by similar triangles
        hypotPixels = math.hypot(self.res_width, self.res_height)
        self.FOV_horz = self.FOV * self.res_width / hypotPixels
        self.FOV_vert = self.FOV * self.res_height / hypotPixels
        
        print("Read camera config for", self.name, "at", self.path)
        print(data)

    # Return (fx, fy, cx, cy) 
    def get_params_april(self):
        return self.cam_matrix[0][0], self.cam_matrix[1][1], self.cam_matrix[0][2], self.cam_matrix[1][2]

        
