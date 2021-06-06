from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from biglietteria.controller.controllerTicket import controllerTicket


class viewVendita(QWidget):
    def __init__(self, widget):
        super(viewVendita, self).__init__()
        self.widget = widget
        #self.controller = controllerTicket()
        self.vista = uic.loadUi("biglietteria/vendita/view/venditabiglietti.ui",self)