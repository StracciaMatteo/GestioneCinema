from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ViewAggiornaDipendente(QWidget):
    def __init__(self, widget,dipendente):
        super(ViewAggiornaDipendente, self).__init__()
        self.widget = widget
        self.dipendente = dipendente
        self.vista_aggiorna_dipendente = uic.loadUi("dipendente/DatiDipendente/view/AggiornaDipendente.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.visualizza_dipendente(dipendente)

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_aggiorna_dipendente)

    def go_home(self):
        self.widget.setCurrentIndex(1)
        self.widget.removeWidget(self.vista_aggiorna_dipendente)

    def visualizza_dipendente(self,dipendente):
        self.vista_aggiorna_dipendente.Nome.setText(dipendente.nome)
        self.vista_aggiorna_dipendente.Cognome.setText(dipendente.cognome)
        self.vista_aggiorna_dipendente.Sesso.setCurrentText(dipendente.sesso)
        #self.vista_aggiorna_dipendente.data_di_nascita.setText(dipendente.data_nascita)
        self.vista_aggiorna_dipendente.Luogo_di_nascita.setText(dipendente.luogo_nascita)
        #self.vista_aggiorna_dipendente.mansione.setText(dipendente.mansione)
        self.vista_aggiorna_dipendente.Codice_fiscale.setText(dipendente.cf)
        self.vista_aggiorna_dipendente.Stipendio.setText(dipendente.stipendio)
        self.vista_aggiorna_dipendente.ID.setText(dipendente.id)
        #self.vista_aggiorna_dipendente.turn_lavoro.setText(dipendente.turno_lavoro)
        #self.vista_aggiorna_dipendente.giorno_libero.setText(dipendente.giorno_libero)
        #self.vista_aggiorna_dipendente.ferie_dal.setText(dipendente.ferie_dal)
        #self.vista_aggiorna_dipendente.ferie_al.setText(dipendente.ferie_al)
        self.vista_aggiorna_dipendente.Commento.setText(dipendente.commento)