from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class app(QWidget):
    
    def __init__(self):
        super().__init__()
        self.version = "1.0.0"
        self.title = "Holy Math"
        self.width = 640
        self.height = 500
    
    def initUI(self):
        FULL_TITLE = self.title + " - " + self.version
        self.setWindowTitle(FULL_TITLE)
        self.setGeometry(0,0,self.width,self.height)
        