from PySide2 import *
relativePathIcons = '../public/icons/'


class StylesExtrinsicCalibration():
    def __init__(self, widget):
        super(StylesExtrinsicCalibration).__init__()
        self.widgetAcq = widget
        self.theme1()
        self.setIcons()
        self.formStyle()

    def theme1(self):
        self.primaryColor = '#f44333'
        self.secondaryColor = '#263238'
        self.buttons = '#00E676'
        self.frameCamera = '#212121'
        self.primaryText = '#f5f5f5'
        self.secondaryText = '#757575'
        self.progressBar = '#ff795e'
        self.lineEdit = '#263238'

    def theme2(self):
        self.primaryColor = '#b90008'
        self.secondaryColor = '#ffffff'
        self.buttons = '#e53935'
        self.frameCamera = '#e0e0e0'
        self.primaryText = '#212121'
        self.secondaryText = '#000a12'
        self.lineEdit = '#f5f5f5'
        self.progressBar = '#ff795e'

    def setIcons(self):
        self.widgetAcq.window.acqButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'video.png'))
        self.widgetAcq.window.acqButton.setIconSize(QtCore.QSize(20, 20))

        self.widgetAcq.window.loadButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'load.png'))
        self.widgetAcq.window.loadButton.setIconSize(QtCore.QSize(20, 20))

        self.widgetAcq.window.startButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'play.png'))
        self.widgetAcq.window.startButton.setIconSize(QtCore.QSize(22, 22))

        self.widgetAcq.window.saveButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'save.png'))
        self.widgetAcq.window.saveButton.setIconSize(QtCore.QSize(17, 17))

        self.widgetAcq.window.previusButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'previous.png'))
        self.widgetAcq.window.previusButton.setIconSize(QtCore.QSize(20, 20))

        self.widgetAcq.window.nextButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'skip.png'))
        self.widgetAcq.window.nextButton.setIconSize(QtCore.QSize(20, 20))

        self.widgetAcq.window.clearButton.setIcon(
            QtGui.QPixmap(relativePathIcons+'refresh.png'))
        self.widgetAcq.window.clearButton.setIconSize(QtCore.QSize(20, 20))

    def formStyle(self):
        styleWindow = """
            QWidget{
                    background: """+self.secondaryColor+""";
                    color:  """+self.primaryText+""";
                    border: none;
                    font: Ubuntu;
                    font-size: 12pt;
                }
                QTabWidget::tab-bar{
                    alignment: right;
                }
                QTabBar{
                    background: """+self.primaryColor+""";
                }
                QTabBar::tab {
                    background: """+self.primaryColor+""";
                    min-width: 10px;
                    margin: 5px;
                    margin-bottom: 10px;
                }
                QTabBar::tab:hover {
                    color: """+self.primaryColor+""";
                }            
                QTabBar::tab:selected {
                    background: """+self.primaryColor+""";
                    Color: """+self.primaryText+""";
                }
                QTabBar::tab:!selected {
                    Color: """+self.secondaryColor+""";
                }
                QTabBar::tab:!selected:hover {
                    Color: """+self.secondaryText+""";
                }
                QPushButton{
                    Background: """+self.buttons + """;
                    Background: """+self.buttons + """;
                    color: """+self.secondaryColor + """;
                    min-height: 40px;
                    min-width: 80px;
                }       
                QPushButton:pressed {
                    background-color: rgb(224, 0, 0);
                    border-style: inset;
                } 
                QPushButton:hover {
                    background-color: #B71C1C;
                    border-style: inset;
                } 
                QComboBox{
                    Background: """+self.secondaryColor + """;
                    color: """+self.primaryText + """;
                    min-height: 25px;
                }        
                QComboBox QAbstractItemView {
                    border: 2px solid darkgray;
                    selection-background-color: lightgray;
                }
                QLineEdit { 
                    Background: """+self.lineEdit + """;    
                    color:  """+self.secondaryText+""";
                    border: 1px solid """+self.primaryColor + """;    
                    text-align: center;
                }
                QLabel {
                    color: """+self.secondaryText + """;
                    font-size: 11pt;
                    font: bold;
                }
                QProgressBar {
                    color: """+self.secondaryText + """;
                    background: """+self.secondaryColor+""";
                    border: none;
                }
                QProgressBar::chunk {
                    color: """+self.progressBar+""";
                    background: """+self.progressBar+""";
                    border: none;
                }                
            """
        self.widgetAcq.setStyleSheet(styleWindow)

        styleHeader = """
            padding-left: 5px;
            background: """+self.primaryColor+""";
            font: bold, Ubuntu sans-serif;
            font-size: 13pt;
            color: """+self.secondaryColor+""";
            min-width:200px;
            padding-bottom: 0;
        """
        self.widgetAcq.window.labelHeader.setStyleSheet(styleHeader)

        styleFrameCamera = """
            background: """+self.frameCamera+""";
            margin: 0;
        """
        self.widgetAcq.window.frameWorkspace.setStyleSheet(styleFrameCamera)

        styleFrameParameters = """
            color: """+self.primaryText+""";
            font: Regular;
        """
        self.widgetAcq.window.textBrowser.setStyleSheet(styleFrameCamera)

        navButtons = """
            background: """+self.frameCamera+""";
            min-height: 30px;
            min-width: 30px;
        """
        self.widgetAcq.window.previusButton.setStyleSheet(navButtons)
        self.widgetAcq.window.nextButton.setStyleSheet(navButtons)


        loadButton = """
            background: """ + self.secondaryColor + """;
            min-height: 24;
            min-width: 33;
            border-radius: 0;
        """
        self.widgetAcq.window.loadButton.setStyleSheet(loadButton)
        self.widgetAcq.window.acqButton.setStyleSheet(loadButton)
