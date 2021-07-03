from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
#classe per visulaizzare tutti i dati del dipendente

class ViewDipendente(QWidget):
    #Costrutore che prende come parametri:
    #Widget: widget principale
    #dipendente: il dipendente da visulizzare
    #callback:metodo callback della classe lista dipendenti per rimouvere il dipendente ed aggiornare la lista dipendente
    #casa: per tornare nella vista Home
    #aggiorna: metodo per passare alla vista aggirna dipendente
    def __init__(self, widget, dipendente, callback, casa, aggiorna):
        super(ViewDipendente, self).__init__()
        self.dipendente = dipendente
        self.widget = widget
        self.callback=callback
        self.casa=casa
        self.aggiorna=aggiorna
        self.vista_dipendente = uic.loadUi("dipendente/DatiDipendente/view/Dipendente.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.visualizza_dipendente(dipendente)
        self.btn_elimina_dip.clicked.connect(self.remove_dipendente)
        self.btn_aggiorna_dip.clicked.connect(self.go_aggiorna_dipendente)

    # metodo per tornare in dietro
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_dipendente)

    # metodo per tornare alla vista Home

    def go_home(self):
        self.widget.setCurrentIndex(1)
        self.widget.removeWidget(self.vista_dipendente)
        self.casa()
    #metodo per passare alla vista aggiorna dipendente una volta viene cliccato il bottone "Aggiorna dipendente"

    def go_aggiorna_dipendente(self):
        self.aggiorna()
        self.widget.removeWidget(self.vista_dipendente)
    #metodo per popolare la vista con i dai del dipendente

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

    #metodo per rimuovere il dipendente ed aggiornare la liasta dipendente

    def remove_dipendente(self):
        self.callback()
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_dipendente)
