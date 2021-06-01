from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox


class VistaInserimentoSpeseRicavi(QWidget):
    def __init__(self, widget):
        super(VistaInserimentoSpeseRicavi,self).__init__()
        self.widget = widget
        self.vista= uic.loadUi("spesericavi/InserimentoSpeseRicavi/Inserisci_Movimento_UI.ui",self)


        self.btn_torna_IM.clicked.connect(self.go_back)
        self.vista.btn_InserisciMov.clicked.connect(self.inserisci_movimento)


    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    def inserisci_movimento(self):
        descrizione=self.vista.lineEdit_DescrizionVoce.text()
        importo= self.vista.lineEdit_Importo.text()
        segno= self.vista.comboBox_Segno.currentText()
        try:
         if float(importo):
            print(descrizione)
            print(segno+importo+"€")
        except(Exception):
            self.box_dialog()

    #Questa funzione apre un MessageBox di errore per l'inserimento errato dell'importo
    def box_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Formato errato")
        msg.setInformativeText("Inserire l'importo corretto")
        msg.setWindowTitle("Errore Importo")
        msg.setStandardButtons(QMessageBox.Ok)
        result = msg.exec()





