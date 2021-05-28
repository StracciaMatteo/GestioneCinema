from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class VistaInserimentoSpeseRicavi(QWidget):
    def __init__(self):
        super(VistaInserimentoSpeseRicavi,self).__init__()
        self.vista= uic.loadUi("spesericavi/InserimentoSpeseRicavi/Inserisci_Movimento_UI.ui",self)
