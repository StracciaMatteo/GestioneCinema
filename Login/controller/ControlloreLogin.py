from PyQt5.QtWidgets import QLineEdit, QMessageBox, QWidget


class ControlloreLogin():

    def __init__(self):
        super(ControlloreLogin, self).__init__()

    def hide_or_show_pw(self, vista):
        vista.Codice.setEchoMode(QLineEdit.Normal)
        if not vista.btn_visibilita_password.isChecked():
            vista.Codice.setEchoMode(QLineEdit.Password)

    def login(self, pw):
        if pw == "prova":
            return True
        else:
            return False
