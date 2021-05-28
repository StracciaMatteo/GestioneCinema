from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLineEdit

from Login.controller.ControlloreLogin import ControlloreLogin
from home.view.VistaHome import VistaHome


class ViewLogin(QWidget):
    def __init__(self, widget):
        super(ViewLogin, self).__init__()
        self.widget = widget
        self.vista = uic.loadUi("Login/View/LoginFinal.ui",self)

        self.controller = ControlloreLogin()

        self.btn_visibilita_password.toggled.connect(self.password_visibility)
        self.btn_Accedi.clicked.connect(self.login)

    def password_visibility(self):
        self.controller.hide_or_show_pw(self.vista)

    def login(self):
        if self.controller.login(self.Codice.text()):
            self.vista.label_error.setText("")
            # inserire utente loggato nella chiamata a VistaHome()
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
            '''vista_home = VistaHome()
            vista_home.show()
            self.vista.setHidden(True)'''
        else:
            self.vista.label_error.setText("Credenziali errate!")
