from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class VistaListaMovimenti(QWidget):
    def __init__(self, widget):
        super(VistaListaMovimenti, self).__init__()
        self.widget = widget
        self.vista= uic.loadUi("spesericavi/view/Lista_Movimenti_UI2.ui", self)
        self.btn_torna_LM.clicked.connect(self.go_back)

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)
