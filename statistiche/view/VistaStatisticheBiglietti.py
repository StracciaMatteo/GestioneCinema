import time
import matplotlib.pyplot as plt
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget
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

    # Questa funzione riceve dal controller della lista film la somma di biglietti venduti per fascia oraria e ne crea un
    # istogramma mostrando a schermo gli istogrammi per fascia oraria,che indicano il numero di biglietti venduti
    def genera_stat(self):
        x= self.controller.get_vendite_giornaliere()
        if x != [0, 0, 0, 0]:
            today = QDate.currentDate()
            if int(time.localtime().tm_hour) < 3:
                today = today.addDays(-1)
            today = today.toString("dd_MM_yyyy")
            label = ["15:00", "18:00", "21:00", "00:00"]
            fig = plt.figure(figsize=(8, 5))
            plt.bar(label, x, color=['maroon', 'red', 'orange', 'yellow'], width=0.5, edgecolor="black")
            plt.xlabel("Orari degli spettacoli ")
            plt.ylabel("Biglietti venduti")
            plt.title("Statistiche sui biglietti venduti "+today)
            plt.tight_layout()
            plt.savefig("statistiche/Statistiche/SatisticheBigietti"+today)
            self.vista.label_stat.setPixmap(QPixmap("statistiche/Statistiche/SatisticheBigietti"+today))



