import json
from util.math_util import Quaternion, Translation


class JetsonData:
    """
    Processed pipeline data to send to the RIO. Initialize this with a `translation` (x, y, z) and quaternion
    `rotation` (w, x, y, z) representing the relative position of the target from the camera, the timestamp
    of the camera frame, the id of the target, and the id of the camera.
    """
    def __init__(self, translation: Translation, rotation: Quaternion, ts: int, tid: int, cid: int):
        self.x = translation[0]
        self.y = translation[1]
        self.z = translation[2]

        self.qw = rotation[0]
        self.qx = rotation[1]
        self.qy = rotation[2]
        self.qz = rotation[3]

        self.ts = ts
        self.tid = tid
        self.cid = cid

    def to_json_str(self):
        """
        Serializes this `JetsonData` object as a JSON string.
        :return: The jetson data as a JSON string.
        """
        return json.dumps(self.__dict__)


if __name__ == '__main__':
    data = JetsonData(
        translation=(1.0, 1.5, 2.4),
        rotation=(1.0, 1.0, 1.0, 1.0),
        ts=100002938,
        tid=16,
        cid=3
    )
    print(data.to_json_str())
