import matplotlib.pyplot as plt
from PyQt5 import uic

from PyQt5.QtWidgets import QWidget
from matplotlib import patches

from listaFilm.controller.controllerListaFilm import controllerListaFilm


class VistaStatisticheBiglietti(QWidget):
    def __init__(self, widget):
        super(VistaStatisticheBiglietti, self).__init__()
        self.widget = widget
        # controller con il metodo get_vendite_giornaliere che restituisce un array di 5 elementi corrispondenti alle
        # sale con valore pari alla somma dei biglietti venduti per ogni spettacolo nella rispettiva sala
        self.controller = controllerListaFilm()
        self.vista = uic.loadUi("statistiche/view/Statistiche_Biglietti_UI2.ui", self)

        self.btn_tornaIndietroSB.clicked.connect(self.go_back)
        self.btn_GeneraDiagramma.clicked.connect(self.genera_stat)

    # Funizone che permette di tornare indietro con il tasto "<-" all'interno della vista
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    # Questa funzione riceve dal controller della lista fil ìm la somma di biglietti venduti per fascia oraria e ne crea un
    # istogramma dividendo le quantità dei biglietti venduti per le varie fascie orarie degli spettacoli
    def genera_stat(self):
        x=[16,17,16,16,16,16,18,21,21,21,21,21,22,15,15,15,18,18,19,19,20,21,25,25,25,25,25,25,25,25,25,25]
        #BINS= ovvero larghezza delle "colonne" dell'istogramma
        number_of_bins=[15,18,21,24,27]
        plt.figure(1)
        names= ["         Spet.1","         Spet.2","         Spet.3","         Spet.4",""]
        n, bins, patches = plt.hist(x,bins= number_of_bins, edgecolor= "black",color="y")
        plt.title("STATISTCHE BIGLIETTI VENDUTI")
        ax= plt.subplot(111)
        ax.set_xticks(number_of_bins)
        ax.set_xticklabels(names,rotation=0, rotation_mode="anchor", va="top",ha="left")
        patches[0].set_fc("y")
        patches[1].set_fc("r")
        patches[2].set_fc("m")
        patches[3].set_fc("c")
        #patches[4].set_fc("b")
        #patches[5].set_fc("w")
        plt.xlabel("Orari")
        plt.ylabel("Numero biglietti venduti")
        plt.legend(patches,names)
        plt.tight_layout()
        plt.show()
