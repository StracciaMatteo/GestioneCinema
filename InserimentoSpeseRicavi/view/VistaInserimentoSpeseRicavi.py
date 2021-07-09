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


    # Questa funzione prende dall'interfaccia
    def add_voce(self):
            descrizione = self.vista.lineEdit_DescrizionVoce.text()
            importo = self.vista.lineEdit_Importo.text()
            segno = self.vista.comboBox_Segno.currentText()
            #model = ModelVoce(segno, importo, descrizione)
            model= ModelVoce(segno,importo,descrizione)
            return model

    # Questa funzione permette il salvataggio dei dati della voce all'interno del file pickle,se i dati sono corretti
    def save(self):
        if self.vista.lineEdit_DescrizionVoce.text():
            try:
                if float(self.vista.lineEdit_Importo.text()):
                    model = self.add_voce()
                    self.controllerInserimentoSR.aggiungi_voce(model)
                    self.go_back()
                    if not self.callback is None:
                        self.callback.clear()
                        for voci in self.controllerInserimentoSR.model.lista_movimenti:
                            self.callback.addItem(voci.segno + str(voci.importo) + "  " + voci.descrizione)
            except ValueError:
                self.box_dialog()
        else:
            self.box_dialog_descrizione()


    # Questa funzione crea un MessageBox di errore per l'inserimento errato dell'importo
    def box_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Formato errato")
        msg.setInformativeText("Inserire l'importo corretto")
        msg.setWindowTitle("Errore Importo")
        msg.setStandardButtons(QMessageBox.Ok)
        result = msg.exec()

    def box_dialog_descrizione(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Formato errato")
        msg.setInformativeText("Inserire la descrizione")
        msg.setWindowTitle("Errore Voce")
        msg.setStandardButtons(QMessageBox.Ok)
        result = msg.exec()




