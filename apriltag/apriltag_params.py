# Reads and stores camera config file (json).

import json
from pathlib import Path


class AprilTagParams:
    def __init__(self, filename):
        print(str(Path(__file__).parent))

        file = open(str(Path(__file__).parent) + '/config/' + filename + '.json')
        data = json.load(file)

        self.tag_size = data['tag_size']
        self.tag_family = data['tag_family']
        self.n_threads = data['n_threads']
        self.quad_decimate = data['quad_decimate']

        self.quad_sigma = data['quad_sigma']
        self.refine_edges = data['refine_edges']
        self.decode_sharpening = data['decode_sharpening']
        self.debug = data['debug']

        print("Read apriltag config for", self.tag_family, "with size", self.tag_size, "meters")
        print(data)

    def set_detection_params(self, tag_size, tag_family, n_threads, quad_decimate, quad_sigma, refine_edges,
                             decode_sharpening, debug):
        self.tag_size = tag_size

        self.tag_family = tag_family
        self.n_threads = n_threads
        self.quad_decimate = quad_decimate
        self.quad_sigma = quad_sigma
        self.refine_edges = refine_edges
        self.decode_sharpening = decode_sharpening
        self.debug = debug
