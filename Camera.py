import cv2
from log import logger
class Camera:
    def __init__(self):
        file = open("./CameraSource.config", "r")
        sr = file.readline().strip()
        self.displayres_res = float(file.readline().strip())
        if len(sr)==1:
            self.source = int(sr)
        else:
            self.source = sr
        file.close()
        self.setup()

    def setup(self):
        try:
            self.cam = cv2.VideoCapture()
            self.cam.open(self.source, cv2.CAP_DSHOW)
            if self.cam is None or not self.cam.isOpened():
                logger.error("no camera at "+self.source)
            self.cam.set(3, 1920)
            self.cam.set(4, 1080)
        except Exception as e:
            logger.error("Camera could not open :"+str(e))


    def CaptureImage(self):
        try:
            ret, img = self.cam.read()
            if ret == False:
                raise Exception("camera read returned False")
            return img, True
        except Exception as e:
            logger.error("Image not captured", str(e))
            img = cv2.imread("./noimage.png",1)
            return img, False