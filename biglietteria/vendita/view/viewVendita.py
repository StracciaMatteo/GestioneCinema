from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from biglietteria.controller.controllerTicket import controllerTicket


class viewVendita(QWidget):
    def __init__(self, widget):
        super(viewVendita, self).__init__()
        self.widget = widget
        #self.controller = controllerTicket()
        self.vista = uic.loadUi("biglietteria/vendita/view/venditabiglietti.ui",self)

        # bottone indietro
        self.vista.btn_torna.clicked.connect(self.go_back)

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)