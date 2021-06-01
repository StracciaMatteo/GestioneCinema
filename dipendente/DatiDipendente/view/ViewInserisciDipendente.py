from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ViewInserisciDipendente(QWidget):
    def __init__(self, widget):
        super(ViewInserisciDipendente, self).__init__()
        self.widget = widget
        self.vista_inserisci_dipendente = uic.loadUi("dipendente/DatiDipendente/view/InserisciDipendente.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_inserisci_dipendente)
    def go_home(self):
        self.widget.setCurrentIndex(1)
        self.widget.removeWidget(self.vista_inserisci_dipendente)

