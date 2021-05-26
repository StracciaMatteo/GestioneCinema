import self as self
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLineEdit


class ViewLogin(QWidget):
    def __init__ (self):
        super(ViewLogin,self).__init__()
        uic.loadUi("Login/View/LoginFinal.ui",self)
        self.btn_visibilita_password.toggled.connect(self.password_visibility)

    def password_visibility(self):
        self.Codice.setEchoMode(QLineEdit.Normal)
        if not self.btn_visibilita_password.isChecked():
            self.Codice.setEchoMode(QLineEdit.Password)
