from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


from biglietteria.rimborso.view.viewRimborso import viewRimborso
from biglietteria.vendita.view.viewVendita import viewVendita
from dipendente.DatiDipendente.view.ViewTurniDiLavoro import ViewTurniDiLavoro
from dipendente.ListaDipendente.view.ViewInserisciDipendente import ViewInserisciDipendente
from dipendente.ListaDipendente.view.ViewListaDipendente import ViewListaDipendente
from film.inserimentoFilm.view.viewInserimentoFilm import viewInserimentoFilm
from listaFilm.visualizzaProgrammazione.view.viewProgrammazione import viewProgrammazione
from InserimentoSpeseRicavi.view.VistaInserimentoSpeseRicavi import VistaInserimentoSpeseRicavi
from spesericavi.view.VistaListaMovimenti import VistaListaMovimenti
from statistiche.view.VistaStatisticheBiglietti import VistaStatisticheBiglietti



class VistaHome(QWidget):
    # il costruttore deve ricevere un oggetto di tipo dipendente per poter stampare il nome dell'utente loggato
    def __init__(self, widget, utente_loggato):
        super(VistaHome, self).__init__()
        self.widget = widget
        self.utente_loggato = utente_loggato
        self.vista = uic.loadUi("home/view/HOME.ui", self)

        # imposta titolo labr in base a utente loggato
        self.vista.label_login_session.setText("Login effettuato da: " + utente_loggato)

        # comando per mostrare o nascondere box gestione dipendenti
        if utente_loggato != "prova":
            self.vista.box_dipendenti.setDisabled(True)
        else:
            self.vista.box_dipendenti.setDisabled(False)

        self.vista.btn_torna.clicked.connect(self.logout)

        # Area Gestione Attività
        self.vista.btn_inserimento_film.clicked.connect(self.visualizza_inserimento_film)
        self.vista.btn_visualizza_programmazione.clicked.connect(self.visualizza_programmazione)

        # Area Gestione Economica
        self.vista.btn_spesa_ricavo.clicked.connect(self.visualizza_ins_spesa_ricavo)
        self.vista.btn_visualizza_movimenti.clicked.connect(self.visualizza_movimenti)
        self.vista.btn_visualizza_statistiche.clicked.connect(self.visualizza_statistiche)

        # Area Gestione Dipendente
        self.vista.btn_inserimento_dipendente.clicked.connect(self.visualizza_inserisci_dipendente)
        self.btn_lista_dipendenti.clicked.connect(self.visualizza_lista_dipendente)
        self.btn_turni_lavoro.clicked.connect(self.visualizza_turni_di_lavoro)
        # Area Biglietteria
        self.vista.btn_vendita_biglietti.clicked.connect(self.vendita_biglietti)
        self.vista.btn_rimborso_biglietti.clicked.connect(self.rimborso_biglietti)

    def logout(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    # Funzioni per accedere a schermate

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

    # Area Gestione Dipendente
    def visualizza_inserisci_dipendente(self):
        vista_listadipendente = ViewListaDipendente(self.widget)
        vista_inseriscidipendente = ViewInserisciDipendente(self.widget,vista_listadipendente.controllerdip,vista_listadipendente.add_dipendente,vista_listadipendente.go_home)
        self.widget.addWidget(vista_inseriscidipendente)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def visualizza_lista_dipendente(self):
        vista_listadipendente = ViewListaDipendente(self.widget)
        self.widget.addWidget(vista_listadipendente)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def visualizza_turni_di_lavoro(self):
        vista_turnilavoro = ViewTurniDiLavoro(self.widget)
        self.widget.addWidget(vista_turnilavoro)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
    # Area Biglietteria

    def vendita_biglietti(self):
        vista_Vendita = viewVendita(self.widget)
        self.widget.addWidget(vista_Vendita)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def rimborso_biglietti(self):
        vista_Rimborso = viewRimborso(self.widget)
        self.widget.addWidget(vista_Rimborso)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
