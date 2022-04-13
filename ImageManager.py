import os
import cv2
from datetime import datetime
import random
class ImageManager:
    def __init__(self):
        self.folder = "./DATACOLLECTOR_DATASET"
        if os.path.exists(self.folder) is False:
            os.mkdir(self.folder)
        self.imagecount, _ = self.getLatestImageCount()
        self.counter = self.imagecount

    def getLatestImageCount(self):
        image_paths = os.listdir(self.folder)
        not_deleted = []
        for im in image_paths:
            if im[-11:-4] != "Deleted":
                not_deleted.append(im)
        self.counter = self.imagecount = len(not_deleted)
        return self.imagecount, len(image_paths)-self.imagecount

    def save_image(self, cvimage, classname):
        self.counter = self.counter + 1
        now = datetime.now()
        date_time = now.strftime("%m-%d-%Y-%H-%M-%S")
        filename = str(self.counter)+classname+"_"+date_time+str(random.randint(0,99999))+".png"
        fullpath = self.folder+"/"+filename
        print(fullpath)
        cv2.imwrite(fullpath,cvimage)
        return self.counter, fullpath
