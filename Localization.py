# takes in multiple individual local estimates from AprilTags and GreenLight
# outputs a estimate of robot's global position by comparing input data and data about the field

class Localization:
    def __init__(self):
        # need to have the positions of each april tag and their ids
        # need to have the positions of the target(s) (or just anything with the reflective green tape)
        return
    
    def localize(self, greenlights, apriltags): 
        # greenlights will be an array of source objects (for camera positions) and their
        # corresponding tuples with predictions (also tuples?)
        # [ (source, (prediction) ), (source, (prediction) ]
        # ex: [ (turretcam, (1,4,3) ), (intakecam, (6,0,3) ) ]

        # apriltags will be the same except the prediction is an array of april tag ids and their estimated positions
        # [ (source, [ (tagid, prediction), (tagid, prediction) ] ), repeat]
        # ex: [ (turretcam, [ (21, 0, 1.5, 1), (12, 1, 2.5, 1) ] ), (intakecam, [ (21, .5, 2, 1), (13, 3, 5, .5) ] ) ]
        return