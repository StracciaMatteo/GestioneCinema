from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from film.inserimentoFilm.view.viewInserimentoFilm import viewInserimentoFilm
from listaFilm.visualizzaProgrammazione.view.viewProgrammazione import viewProgrammazione
from spesericavi.InserimentoSpeseRicavi.VistaInserimentoSpeseRicavi import VistaInserimentoSpeseRicavi
from spesericavi.view.VIstaListaMovimenti import VistaListaMovimenti
from statistiche.view.VistaStatisticheBiglietti import VistaStatisticheBiglietti


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

        # Area Gestione Attività
        self.vista.btn_inserimento_film.clicked.connect(self.visualizza_inserimento_film)
        self.vista.btn_visualizza_programmazione.clicked.connect(self.visualizza_programmazione)

        # Area Gestione Economica
        self.vista.btn_spesa_ricavo.clicked.connect(self.visualizza_ins_spesa_ricavo)
        self.vista.btn_visualizza_movimenti.clicked.connect(self.visualizza_movimenti)
        self.vista.btn_visualizza_statistiche.clicked.connect(self.visualizza_statistiche)

    def logout(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    # Funzioni per accedere a schermate

    '''def prova(self):
        vista_prova = ViewDipendente(self.widget)
        self.widget.addWidget(vista_prova)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)'''

    # Area Gestione Attività
    def visualizza_inserimento_film(self):
        vista_inserimento_film = viewInserimentoFilm(self.widget)
        self.widget.addWidget(vista_inserimento_film)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def visualizza_programmazione(self):
        vista_programmazione = viewProgrammazione(self.widget)
        self.widget.addWidget(vista_programmazione)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    # Area Gestione Economica
    def visualizza_ins_spesa_ricavo(self):
        vista_ins_spesa_ricavo = VistaInserimentoSpeseRicavi(self.widget)
        self.widget.addWidget(vista_ins_spesa_ricavo)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def visualizza_movimenti(self):
        vista_movimenti = VistaListaMovimenti(self.widget)
        self.widget.addWidget(vista_movimenti)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def visualizza_statistiche(self):
        vista_statistiche = VistaStatisticheBiglietti(self.widget)
        self.widget.addWidget(vista_statistiche)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

