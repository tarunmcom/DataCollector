import os.path


class Manager:
    def __init__(self):
        self.filename = "./classes.csv"
        if os.path.exists(self.filename) is False:
            f = open(self.filename,"w")
            f.close()


    def readClasses(self):
        file = open(self.filename,'r')
        classes = file.readlines()
        file.close()
        classes = [m.strip() for m in classes]
        return sorted(classes)

    def addClasses(self,classes):
        #TODO better to trip space recursively and check there should not be only spaces
        #TODO check class already exist , word similarity
        classes = classes.split(',')
        writecount = 0
        if len(classes) > 0:
            classes = [m.strip().title() for m in classes]
            filew = open(self.filename,'a')
            for cls in classes:
                spccount = cls.count(' ')
                tbcount = cls.count('\t')
                length = len(cls)
                goodletters = length-(spccount+tbcount)
                if goodletters>0:
                    filew.write(cls+"\n")
                    writecount = writecount + 1
            filew.close()
            return writecount

