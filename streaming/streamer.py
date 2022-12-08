import cv2 as cv
import gst



class Streamer:
    def __init__(self, port):
        self.port = port
        self.queue = []
        self.streamer = gst.parse_launch("v4l2src ! video/x-raw-yuv,width=128,height=96,format='(fourcc)'UYVY ! videoconvert ! ffenc_h263 ! video/x-h263 ! rtph263ppay pt=96 ! udpsink host=192.168.1.1 port=" + self.port + "sync=false")
        self.streamer.set_state(4) #starts the pipeline
        # function gotten from
        # https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html?gi-language=c

        self.buffer = gst.Buffer()

    def run(self):
        if(self.queue.len() > 0):
            img = self.queue.pop(0)
            self.buffer.append(img)

        else:
            return
        
        #
    
    def sendimg(self, img):
        self.queue.append(img)

    