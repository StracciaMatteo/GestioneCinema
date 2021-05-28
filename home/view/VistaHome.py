from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class VistaHome(QWidget):
    # il costruttore deve ricevere un oggetto di tipo dipendente per poter stampare il nome dell'utente loggato
    def __init__(self):
        super(VistaHome, self).__init__()
        self.vista = uic.loadUi("home/view/HOME.ui", self)
        self.vista.label_login_session.setText("Login effettuato da: PROVA")    # MODIFICARE
        # comando per mostrare o nascondere box gestione dipendenti
        # self.vista.box_dipendenti.hide()

        self.vista.btn_torna.clicked.connect(self.logout)

    def logout(self):
        self.vista.close()
