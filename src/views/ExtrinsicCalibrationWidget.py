
from PySide2 import QtWidgets, QtCore, QtUiTools
import sys
import os


from StylesExtrinsicCalibration import StylesExtrinsicCalibration


class ExtrinsicCalibrationWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(ExtrinsicCalibrationWidget, self).__init__(*args, **kwargs)
        self.loadForm()
        self.initUI()
        StylesExtrinsicCalibration(self)

    def initUI(self):
        self.setWindowTitle("Extrinsic Calibration")
        self.setGeometry(200, 50, 900, 635)

    def loadForm(self):
        formUI = os.path.join(sys.path[0], 'views/extrinsicCalibration.ui')
        file = QtCore.QFile(formUI)        
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader()
        self.window = loader.load(file)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.window)
        self.setLayout(layout)

