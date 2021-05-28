from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class VistaStatisticheBiglietti(QWidget):
    def __init__(self):
        super(VistaStatisticheBiglietti,self).__init__()
        self.vista= uic.loadUi("statistiche/view/Statistiche_Biglietti_UI2.ui",self)


