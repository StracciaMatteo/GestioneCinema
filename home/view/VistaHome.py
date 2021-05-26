from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class VistaHome(QWidget):
    def __init__(self):
        super(VistaHome, self).__init__()
        self.vista = uic.loadUi("home/view/HOME.ui", self)
