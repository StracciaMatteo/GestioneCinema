from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from listaFilm.controller.controllerListaFilm import controllerListaFilm


# from biglietteria.controller.controllerTicket import controllerTicket


class viewRimborso(QWidget):
    def __init__(self, widget):
        super(viewRimborso, self).__init__()
        self.widget = widget
        self.controller = controllerListaFilm()
        self.vista = uic.loadUi("biglietteria/rimborso/view/Rimborso.ui", self)

        #bottone indietro
        self.vista.btn_torna.clicked.connect(self.go_back)


        self.vista.procedi.clicked.connect(self.rimborsa_biglietto)

    # la funzione permette di rimborsare uno spettacolo tramite il codice se tutte le condizioni sono rispettate
    def rimborsa_biglietto(self):
        codice = self.vista.codice.text()
        self.controller.rimborsa_biglietto(codice)

    # Funzione che permette di tornare indietro con il tasto "<-" all'interno della vista
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)
        self.controller.save()

