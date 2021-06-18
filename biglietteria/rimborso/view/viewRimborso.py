from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from listaFilm.controller.controllerListaFilm import controllerListaFilm


from biglietteria.controller.controllerTicket import controllerTicket


class viewRimborso(QWidget):
    def __init__(self, widget):
        super(viewRimborso, self).__init__()
        self.widget = widget
        # self.controller = controllerTicket()
        self.vista = uic.loadUi("biglietteria/rimborso/view/Rimborso.ui", self)

        #bottone indietro
        self.vista.btn_torna.clicked.connect(self.go_back)

        self.vista.btn_procedi.clicked.connect(self.rimborsa_biglietto(self, codice_univoco))




    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    '''
    per rimborsare, dopo la pressione del bottone 'procedi' passare alla funzione rimborso_biglietto del controller 
    listaFilm il codice univoco letto dalla LineEdit e il rimborso verrà fatto automaticamente se lo spettacolo esiste 
    e il codice è corretto. Chiamare la funzione save del controller per salvare la nuova situazione di disponibilità
    dei posti
    '''