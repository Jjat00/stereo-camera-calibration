from ControllerExtrinsicCalibration import *

class ViewExtrinsicCalibration():
    def __init__(self, window):
        super(ViewExtrinsicCalibration).__init__()
        self.window = window
        self.controllerIntrinsicCalibration = ControllerExtrinsicCalibration(self.window)

    def connectAcqButton(self):
        self.window.acqButton.clicked.connect(
            self.controllerIntrinsicCalibration.handlerAcquisitionImage)

    def connectLoadButton(self):
        self.window.loadButton.clicked.connect(
            self.controllerIntrinsicCalibration.handlerLoadPatternImages)

    def connectStartButton(self):
        self.window.startButton.clicked.connect(
            self.controllerIntrinsicCalibration.handlerStartCalibration)

    def connectSaveButton(self):
        self.window.saveButton.clicked.connect(
            self.controllerIntrinsicCalibration.handlerSaveParameters)

    def connectPreviousButton(self):
        self.window.previusButton.clicked.connect(
            self.controllerIntrinsicCalibration.handlerPreviousParameters)

    def connectNextButton(self):
        self.window.nextButton.clicked.connect(
            self.controllerIntrinsicCalibration.handlerNextParameters)

    def connectClearButton(self):
        self.window.clearButton.clicked.connect(
            self.controllerIntrinsicCalibration.handlerClearWorkspace)

