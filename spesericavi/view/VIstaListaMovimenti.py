from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class VistaListaMovimenti(QWidget):
    def __init__(self, widget):
        super(VistaListaMovimenti, self).__init__()
        self.widget = widget
        self.vista= uic.loadUi("spesericavi/view/Lista_Movimenti_UI2.ui", self)
