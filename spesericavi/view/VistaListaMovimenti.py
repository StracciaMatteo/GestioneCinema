from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from InserimentoSpeseRicavi.view.VistaInserimentoSpeseRicavi import VistaInserimentoSpeseRicavi


class VistaListaMovimenti(QWidget):
    def __init__(self, widget):
        super(VistaListaMovimenti, self).__init__()
        self.widget = widget
        self.vista= uic.loadUi("spesericavi/view/Lista_Movimenti_UI2.ui", self)
        self.btn_torna_LM.clicked.connect(self.go_back)
        self.btn_InserisciMovLM.clicked.connect(self.apri_inserisci_voce)


    def apri_inserisci_voce(self):
        inserisci_voce = VistaInserimentoSpeseRicavi(self.widget)
        self.widget.addWidget(inserisci_voce)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)
