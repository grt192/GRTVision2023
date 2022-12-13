# https://github.com/SouthwestRoboticsProgramming/TagTracker/blob/master/src/quaternions.py

import math
from typing import Tuple

Translation = Tuple[float, float, float]
Quaternion = Tuple[float, float, float, float]


def matrix_to_quat(m) -> Quaternion:
    """
    Converts a 3x3 rotation matrix to a quaternion.
    :param m: The 3x3 rotation matrix.
    :return: The quaternion, as a tuple of [w, x, y, z].
    """
    r11 = m[0][0]; r12 = m[0][1]; r13 = m[0][2]
    r21 = m[1][0]; r22 = m[1][1]; r23 = m[1][2]
    r31 = m[2][0]; r32 = m[2][1]; r33 = m[2][2]

    trace = r11 + r22 + r33
    if trace > 0:
        s = 0.5 / math.sqrt(trace + 1.0)
        w = 0.25 / s
        x = (r32 - r23) * s
        y = (r13 - r31) * s
        z = (r21 - r12) * s
    else:
        if r11 > r22 and r11 > r33:
            s = 2.0 * math.sqrt(1.0 + r11 - r22 - r33)
            w = (r32 - r23) / s
            x = 0.25 * s
            y = (r12 + r21) / s
            z = (r13 + r31) / s
        elif r22 > r33:
            s = 2.0 * math.sqrt(1.0 + r22 - r11 - r33)
            w = (r13 - r31) / s
            x = (r12 + r21) / s
            y = 0.25 * s
            z = (r23 + r32) / s
        else:
            s = 2.0 * math.sqrt(1.0 + r33 - r11 - r22)
            w = (r21 - r12) / s
            x = (r13 + r31) / s
            y = (r23 + r32) / s
            z = 0.25 * s

    return w, x, y, z


if __name__ == "__main__":
    rot = (
        (0.6112, -0.7903, 0.0429),
        (0.6788, 0.5515, 0.4846),
        (-0.4068, -0.2671, 0.8736)
    )

    print(matrix_to_quat(rot))
