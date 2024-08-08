import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from check_db import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui.setupUi(self)

    def setu(self):
        uic.loadUi('assets/main/MainWindow.ui', self)
