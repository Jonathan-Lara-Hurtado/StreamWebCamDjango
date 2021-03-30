import numpy as np
import cv2
import threading


class VideoCamera(object):

    disponible = False

    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.disponible = self.video.isOpened()
#        (self.grabbed, self.frame) = self.video.read()
 #       threading.Thread(target=self.update, args=()).start()

    def get_disponible(self):
        return self.disponible

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        (self.grabbed, self.frame) = self.video.read()
        _, jpeg = cv2.imencode('.jpg', self.frame)
        return jpeg.tobytes()
    
 #   def update(self):
  #      while True:
   #         (self.grabbed, self.frame) = self.video.read()