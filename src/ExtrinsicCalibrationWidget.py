"""
File: ExtrinsicCalibrationWidget.py
Author: Jaimen Aza <<Jjat userjjar00@gmail.com>>
Date create: 21-august-2020
Last moditication date : 21-august-2020
"""

import sys
import os

dirs = ['views', 'styles', 'controllers', 'models',
        'components/AcquisitionExtrinsicCalibration/src/']

for nameDir in dirs:
    path = os.path.join(sys.path[0], nameDir)
    sys.path.append(path)


import cv2
from PySide2 import *
from StylesIntrinsicCalibration import *
from ViewExtrinsicCalibration import *

class ExtrinsicCalibrationWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(ExtrinsicCalibrationWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.ViewExtrinsicCalibration = ViewExtrinsicCalibration(self.window)
        self.initUI()
        StylesIntrinsicCalibration(self)

    def initUI(self):
        self.setWindowTitle("Extrinsic Calibration")
        self.setGeometry(200, 50, 900, 635)
        self.connectButtons()

    def loadForm(self):
        formUI = os.path.join(sys.path[0], 'views/extrinsicCalibration.ui')
        file = QtCore.QFile(formUI)        
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)

    def connectButtons(self):
        self.ViewExtrinsicCalibration.connectAcqButton()
        self.ViewExtrinsicCalibration.connectLoadButton()
        self.ViewExtrinsicCalibration.connectStartButton()
        self.ViewExtrinsicCalibration.connectSaveButton()
        self.ViewExtrinsicCalibration.connectPreviousButton()
        self.ViewExtrinsicCalibration.connectNextButton()
        self.ViewExtrinsicCalibration.connectClearButton()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    acquisitionExtrinsicCalibration = ExtrinsicCalibrationWidget()
    acquisitionExtrinsicCalibration.show()
    app.exec_()
