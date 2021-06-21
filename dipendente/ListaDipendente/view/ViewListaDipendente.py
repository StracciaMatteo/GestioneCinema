from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QListWidgetItem

from dipendente.DatiDipendente.view.ViewDipendente import ViewDipendente
from dipendente.ListaDipendente.controller.ControllerListaDipendenti import ControllerListaDipendenti
from dipendente.ListaDipendente.view.ViewInserisciDipendente import ViewInserisciDipendente


class ViewListaDipendente(QWidget):
    def __init__(self, widget):
        super(ViewListaDipendente, self).__init__()
        self.widget = widget
        self.controllerdip = ControllerListaDipendenti()
        self.vista_lista_dipendente = uic.loadUi("dipendente/ListaDipendente/view/ListaDipendenti.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.btn_inserisci_dip.clicked.connect(self.go_inserisci_dipendente)
        #self.btn_ricerca.clicked.connect(self.search_dipendente)
        self.popola_lista_dipententi()
        self.list_dipendenti.itemDoubleClicked.connect(self.go_view_dipendente)
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_lista_dipendente)

    def go_home(self):
        self.widget.setCurrentIndex(1)
        self.widget.removeWidget(self.vista_lista_dipendente)

    def go_to(self, vista):
        self.widget.addWidget(vista)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        vista.btn_Home.clicked.connect(self.go_home)

    def go_inserisci_dipendente(self):
        vista_inseriscidipendente = ViewInserisciDipendente(self.widget)
        self.go_to(vista_inseriscidipendente)

    def popola_lista_dipententi(self):
        self.vista_lista_dipendente.list_dipendenti.setSortingEnabled(True)
        for dipendente in self.controllerdip.modeldip.listdipendent:
            self.vista_lista_dipendente.list_dipendenti.addItem(dipendente.cognome+" "+dipendente.nome)

    def go_view_dipendente(self):
        cognome=self.vista_lista_dipendente.list_dipendenti.currentItem().text()
        dipendente=self.controllerdip.get_dipendente_by_name(cognome.split()[0])
        viewdipendente=ViewDipendente(self.widget,dipendente)
        self.go_to(viewdipendente)
    '''def search_dipendente(self):
        item=self.vista_lista_dipendente.list_dipendenti.findItems(self.vista_lista_dipendente.barra_ricerca.text(),Qt.MatchContains)
        for dipendente in self.controllerdip.modeldip.listdipendent:
            if dipendente.cognome.split()[0]==self.vista_lista_dipendente.barra_ricerca.text():
                print("done")
            else:
                print("non trovato")'''