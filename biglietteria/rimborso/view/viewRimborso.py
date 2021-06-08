from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from biglietteria.controller.controllerTicket import controllerTicket


class viewRimborso(QWidget):
    def __init__(self, widget):
        super(viewRimborso, self).__init__()
        self.widget = widget
        # self.controller = controllerTicket()
        self.vista = uic.loadUi("biglietteria/rimborso/view/Rimborso.ui", self)