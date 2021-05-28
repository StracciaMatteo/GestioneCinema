from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from dipendente.DatiDipendente.view.ViewDipendente import ViewDipendente


class VistaHome(QWidget):
    # il costruttore deve ricevere un oggetto di tipo dipendente per poter stampare il nome dell'utente loggato
    def __init__(self, widget):
        super(VistaHome, self).__init__()
        self.widget = widget
        self.vista = uic.loadUi("home/view/HOME.ui", self)
        self.vista.label_login_session.setText("Login effettuato da: PROVA")    # MODIFICARE
        # comando per mostrare o nascondere box gestione dipendenti
        # self.vista.box_dipendenti.setDisabled(True)

        self.vista.btn_torna.clicked.connect(self.logout)
        # self.btn_inserimento_film.clicked.connect(self.prova)

    def logout(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    # Funzioni per accedere a schermate

    '''def prova(self):
        vista_prova = ViewDipendente(self.widget)
        self.widget.addWidget(vista_prova)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)'''

