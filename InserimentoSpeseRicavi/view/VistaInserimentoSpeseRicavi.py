from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox
from InserimentoSpeseRicavi.controller.ControlloreInserimentoSR import ControlloreInserimentoSR
from InserimentoSpeseRicavi.model.ModelVoce import ModelVoce


class VistaInserimentoSpeseRicavi(QWidget):

    def __init__(self,widget,callback):
        super(VistaInserimentoSpeseRicavi, self).__init__()
        self.widget = widget
        self.callback = callback
        self.controllerInserimentoSR = ControlloreInserimentoSR()
        self.vista = uic.loadUi("InserimentoSpeseRicavi/view/Inserisci_Movimento_UI.ui", self)
        self.btn_torna_IM.clicked.connect(self.go_back)
        self.vista.btn_InserisciMov.clicked.connect(self.save)
        self.vista.btn_InserisciMov.setShortcut("Return")

    # Funizone che permette di tornare indietro con il tasto "<-" all'interno della vista
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    # Questa funzione prende dall'interfaccia i dati e ne controlla il corretto inserimento, in caso di inserimento errato
    # visualizza a schermo un Box dialog di errore
    def add_voce(self):
        descrizione=self.vista.lineEdit_DescrizionVoce.text()
        importo=self.vista.lineEdit_Importo.text()
        segno= self.vista.comboBox_Segno.currentText()
        try:
            if (float(importo) != "" or descrizione != ""):
                print(descrizione)
                print(segno+importo+"€")
        except:
            self.box_dialog()
        model= ModelVoce(segno,importo,descrizione)
        return model

    # Questa funzione permette il salvataggio dei dati della voce all'interno del file pickle
    def save(self):
        model = self.add_voce()
        self.controllerInserimentoSR.aggiungi_voce(model)
        self.go_back()
        if not self.callback is None:
            for voci in self.controllerInserimentoSR.model.lista_movimenti:
                self.callback.addItem(voci.segno + str(voci.importo) + "  " + voci.descrizione)


    # Questa funzione crea un MessageBox di errore per l'inserimento errato dell'importo
    def box_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Formato errato")
        msg.setInformativeText("Inserire l'importo corretto")
        msg.setWindowTitle("Errore Importo")
        msg.setStandardButtons(QMessageBox.Ok)
        result = msg.exec()





