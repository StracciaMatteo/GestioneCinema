from PyQt5.QtWidgets import QMessageBox


class Error():
    def __init__(self, titolo, messaggio, testo_alternativo):
        super(Error, self).__init__()
        self.msg = QMessageBox()
        self.msg.setText(messaggio)
        self.msg.setInformativeText(testo_alternativo)
        self.msg.setWindowTitle(titolo)

    def error_messagge(self):
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setStandardButtons(QMessageBox.Ok)
        return self.msg.exec()

    def confirm_messagge(self):
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        return self.msg.exec()

    def warning_messagge(self):
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setStandardButtons(QMessageBox.Ok)
        return self.msg.exec()

