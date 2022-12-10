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

    q0 = math.sqrt((1 - r11 - r22 + r33) / 4)
    q1 = math.sqrt((1 + r11 + r22 + r33) / 4)
    q2 = math.sqrt((1 + r11 - r22 - r33) / 4)
    q3 = math.sqrt((1 - r11 + r22 - r33) / 4)

    if q1 > q2 and q1 > q3 and q1 > q0:
        q2 = (r32 - r23) / (4 * q1)
        q3 = (r13 - r31) / (4 * q1)
        q0 = (r21 - r12) / (4 * q1)
    elif q2 > q1 and q2 > q3 and q2 > q0:
        q1 = (r32 - r23) / (4 * q2)
        q3 = (r12 + r21) / (4 * q2)
        q0 = (r13 + r31) / (4 * q2)
    elif q3 > q1 and q3 > q2 and q3 > q0:
        q1 = (r13 - r31) / (4 * q3)
        q2 = (r12 + r21) / (4 * q3)
        q0 = (r23 + r32) / (4 * q3)
    elif q0 > q1 and q0 > q2 and q0 > q3:
        q1 = (r21 - r12) / (4 * q0)
        q2 = (r13 + r31) / (4 * q0)
        q3 = (r23 + r32) / (4 * q0)

    return q0, q1, q2, q3


def invert_quat(q: Quaternion) -> Quaternion:
    """
    Inverts a quaternion.
    :param q: The quaternion to invert, as a tuple of [w, x, y, z].
    :return: The inverted quaternion.
    """
    return -q[0], q[1], -q[2], -q[3]
