import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox

from InserimentoSpeseRicavi.controller.ControlloreInserimentoSR import ControlloreInserimentoSR
from InserimentoSpeseRicavi.model.ModelVoce import ModelVoce


class VistaInserimentoSpeseRicavi(QWidget):
    def __init__(self, widget):
        super(VistaInserimentoSpeseRicavi,self).__init__()
        self.widget = widget
        self.controllerInserimentoSR= ControlloreInserimentoSR()
        self.vista= uic.loadUi("InserimentoSpeseRicavi/view/Inserisci_Movimento_UI.ui",self)
        self.btn_torna_IM.clicked.connect(self.go_back)
        self.vista.btn_InserisciMov.clicked.connect(self.save)


    #Funzione che fa "scorrere" il widget all'indice precedente
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)
    #Questa funzione prende dall'interfaccia i dati e salva la voce nella lista delle voci di spese e ricavi
    def add_voce(self):
        descrizione=self.vista.lineEdit_DescrizionVoce.text()
        importo=float(self.vista.lineEdit_Importo.text())
        segno= self.vista.comboBox_Segno.currentText()
        try:
            if (float(importo) != "" or descrizione != "" ):
                print(descrizione)
                print(segno+importo+"€")
        except TypeError:
            self.box_dialog()
        model= ModelVoce(segno,importo,descrizione)
        return model

    #Questa funzione implementa il salvataggio dei dati della voce
    def save(self):
        self.controllerInserimentoSR.aggiungi_voce(self.add_voce())
        self.controllerInserimentoSR.save()

    #Questa funzione apre un MessageBox di errore per l'inserimento errato dell'importo
    def box_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Formato errato")
        msg.setInformativeText("Inserire l'importo corretto")
        msg.setWindowTitle("Errore Importo")
        msg.setStandardButtons(QMessageBox.Ok)
        result = msg.exec()





