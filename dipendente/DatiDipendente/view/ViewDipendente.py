from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ViewDipendente(QWidget):
    def __init__(self, widget,dipendente,callback):
        super(ViewDipendente, self).__init__()
        self.dipendente = dipendente
        self.widget = widget
        self.callback=callback
        self.vista_dipendente = uic.loadUi("dipendente/DatiDipendente/view/Dipendente.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.visualizza_dipendente(dipendente)
        self.btn_elimina_dip.clicked.connect(self.remove_dipendente)

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_dipendente)

    def go_home(self):
        self.widget.setCurrentIndex(1)
        self.widget.removeWidget(self.vista_dipendente)

    def visualizza_dipendente(self,dipendente):
        self.nome.setText(dipendente.nome)
        self.cognome.setText(dipendente.cognome)
        self.sesso.setText(dipendente.sesso)
        self.data_di_nascita.setText(dipendente.data_nascita)
        self.luogo_di_nascita.setText(dipendente.luogo_nascita)
        self.mansione.setText(dipendente.mansione)
        self.codice_fiscale.setText(dipendente.cf)
        self.stipendio.setText(dipendente.stipendio)
        self.id.setText(dipendente.id)
        self.turn_lavoro.setText(dipendente.turno_lavoro)
        self.giorno_libero.setText(dipendente.giorno_libero)
        self.ferie_dal.setText(dipendente.ferie_dal)
        self.ferie_al.setText(dipendente.ferie_al)
        self.commento.setText(dipendente.commento)
    def remove_dipendente(self):
        self.callback()
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_dipendente)
