import matplotlib.pyplot as plt
from PyQt5 import uic

from PyQt5.QtWidgets import QWidget


class VistaStatisticheBiglietti(QWidget):
    def __init__(self, widget):
        super(VistaStatisticheBiglietti, self).__init__()
        self.widget = widget
        self.vista = uic.loadUi("statistiche/view/Statistiche_Biglietti_UI2.ui", self)

        self.btn_tornaIndietroSB.clicked.connect(self.go_back)
        self.btn_GeneraDiagramma.clicked.connect(self.genera_stat)

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    def genera_stat(self):
        x=[15,16,18,17,17,17,18,19,15,16,16,16,16,16,14,17,18,18,18,22,22,23,24,24,26,25,24]
        #BINS= ovvero larghezza delle "colonne" dell'istogramma
        number_of_bins=[14,16,18,20,22,24,26]
        plt.figure(1)
        plt.hist(x,bins= number_of_bins, edgecolor= "black",color="y")
        plt.title("STATISTCHE BIGLIETTI VENDUTI")
        plt.xlabel("Orari")
        plt.ylabel("Numero biglietti venduti")
        plt.show()
