# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.2.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import logging
import os
import winsound

import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from Camera import Camera
from log import logger
from ClassManager import Manager
from AddClass import Ui_form_addClass
from ImageManager import  ImageManager


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon('./ai.ico'))
        MainWindow.resize(782, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.gridLayout_3.setContentsMargins(6, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelImage = QtWidgets.QLabel(self.centralwidget)
        self.labelImage.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.labelImage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelImage.setObjectName("labelImage")
        self.gridLayout_3.addWidget(self.labelImage, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 5, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.combo_Class = QtWidgets.QComboBox(self.centralwidget)
        self.combo_Class.setMinimumSize(QtCore.QSize(0, 95))
        self.combo_Class.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(False)
        self.combo_Class.setFont(font)
        self.combo_Class.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.combo_Class.setAutoFillBackground(False)
        self.combo_Class.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.combo_Class.setCurrentText("")
        self.combo_Class.setObjectName("combo_Class")
        self.verticalLayout.addWidget(self.combo_Class)
        self.lbl_Count = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Count.setMinimumSize(QtCore.QSize(0, 200))
        self.lbl_Count.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.lbl_Count.setFont(font)
        self.lbl_Count.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.lbl_Count.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_Count.setObjectName("lbl_Count")
        self.verticalLayout.addWidget(self.lbl_Count)
        self.btn_Capture = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Capture.setMinimumSize(QtCore.QSize(0, 200))
        self.btn_Capture.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_Capture.setFont(font)
        self.btn_Capture.setStyleSheet("background-color: rgb(85, 231, 22);")
        icon = QtGui.QIcon.fromTheme("camera")
        self.btn_Capture.setIcon(icon)
        self.btn_Capture.setObjectName("btn_Capture")
        self.verticalLayout.addWidget(self.btn_Capture)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_Delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Delete.setMinimumSize(QtCore.QSize(0, 75))
        self.btn_Delete.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_Delete.setFont(font)
        self.btn_Delete.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btn_Delete.setObjectName("btn_Delete")
        self.verticalLayout.addWidget(self.btn_Delete)


        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_Class = QtGui.QAction(MainWindow)
        self.actionAdd_Class.setObjectName("actionAdd_Class")
        self.menuFile.addAction(self.actionAdd_Class)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ### OTHER THAN GUI ELEMENTS
        self.setup_connections()
        self.camera = Camera()
        self.image = None
        self.classManager = Manager()
        self.get_refresh_classList()
        self.image_manager = ImageManager() ##TODo put in configfile
        self.image_count = self.image_manager.counter
        self.lbl_Count.setText(str(self.image_count))
        self.last_img_path = None

    def get_refresh_classList(self):
        self.combo_Class.clear()
        self.combo_Class.addItems(self.classManager.readClasses())


    def on_menu_addClass(self):
        form_addClass = QtWidgets.QDialog()
        ui = Ui_form_addClass()
        ui.setupUi(form_addClass)
        form_addClass.exec()
        self.get_refresh_classList()

    def show_message(self,msg, title):
        dlg = QtWidgets.QMessageBox()
        dlg.setWindowIcon(QtGui.QIcon('./ai.ico'))
        dlg.setText(msg)
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.setWindowTitle(title)
        dlg.defaultButton()
        dlg.exec()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelImage.setText(_translate("MainWindow", "No Image"))
        self.combo_Class.setPlaceholderText(_translate("MainWindow", "Select Class"))
        self.lbl_Count.setText(_translate("MainWindow", "Count"))
        self.btn_Capture.setText(_translate("MainWindow", "&Capture"))
        self.btn_Delete.setText(_translate("MainWindow", "&Delete"))
        self.menuFile.setTitle(_translate("MainWindow", "&File"))
        self.actionAdd_Class.setText(_translate("MainWindow", "&Add Class"))


    def setup_connections(self):
        self.btn_Capture.clicked.connect(self.onBtnClicked_Capture)
        self.actionAdd_Class.triggered.connect(self.on_menu_addClass)
        self.btn_Delete.clicked.connect(self.onBtnClicked_Delete)

    def onBtnClicked_Delete(self):
        if self.last_img_path is not None:
            newpath = self.last_img_path[:-4]+"Deleted"+".png"
            os.rename(self.last_img_path,newpath)
            self.last_img_path = None
            self.labelImage.setText("Last One Deleted")
            self.image_count, _ = self.image_manager.getLatestImageCount()
            self.lbl_Count.setText(str(self.image_count))
        else:
            self.labelImage.setText("No last image to delete")



    #slots
    def onBtnClicked_Capture(self):
        id = self.combo_Class.currentIndex()
        if id == -1:
            self.show_message("Please select a class from the drop down menu.", "Select A Class")
            return
        self.image, found = self.camera.CaptureImage()
        if found==False:
            self.qimage = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0],
            QtGui.QImage.Format.Format_RGB888).rgbSwapped()
            self.labelImage.setPixmap(QtGui.QPixmap.fromImage(self.qimage))
            logger.error("Could not capture image")
            self.show_message("Could not capture image. Please check if camera is connected @ code:"+str(self.camera.source)+"\n Please modify first line of CameraSource.config with correct camera code (or source string) if this code is wrong", "No Image")
            return
        if self.image is not None:
            try:
                width = int(self.image.shape[1] * self.camera.displayres_res)
                height = int(self.image.shape[0] * self.camera.displayres_res)
                dim = (width, height)
                display_image = cv2.resize(self.image.copy(), dim)
                self.qimage = QtGui.QImage(display_image.data, display_image.shape[1], display_image.shape[0], QtGui.QImage.Format.Format_RGB888).rgbSwapped()
                self.labelImage.setPixmap(QtGui.QPixmap.fromImage(self.qimage))
                selected_class = self.combo_Class.currentText()
                self.image_count, self.last_img_path = self.image_manager.save_image(self.image,selected_class)
                self.lbl_Count.setText(str(self.image_count))
                winsound.MessageBeep()
            except Exception as e:
                logger.error("Image not shown in label or not saved:, ", str(e))

        else:
            logging.error("Image was None")



if __name__ == "__main__":
    import sys
    print("1")
    app = QtWidgets.QApplication(sys.argv)
    print("2")
    MainWindow = QtWidgets.QMainWindow()
    print("3")
    ui = Ui_MainWindow()
    print("4")
    ui.setupUi(MainWindow)
    print("5")
    MainWindow.showMaximized()
    print("6")
    sys.exit(app.exec())
    print("7")
