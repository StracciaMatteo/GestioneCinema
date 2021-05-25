from PyQt5 import uic
from PyQt5.QtWidgets import QWidget



class ViewLogin(QWidget):
    def __init__ (self):
        super().__init__()
        uic.loadUi("Login/View/LoginFinal.ui",self)

