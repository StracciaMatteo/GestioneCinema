from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidget

from spesericavi.view.VistaListaMovimenti import VistaListaMovimenti


class VistaInserimentoSpeseRicavi(QWidget):
    def __init__(self, widget):
        super(VistaInserimentoSpeseRicavi,self).__init__()
        self.widget = widget
        self.vista= uic.loadUi("spesericavi/InserimentoSpeseRicavi/Inserisci_Movimento_UI.ui",self)


        self.btn_torna_IM.clicked.connect(self.go_back)
        self.vista.btn_InserisciMov.clicked.connect(self.inserisci_movimento)

    #Funzione che torna alla pagina precedente
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)
    #
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

        tabella = VistaListaMovimenti.vista.table_ListaMov
        lastrow = tabella.rowCount()
        tabella.insertRow(lastrow)
        item = QTableWidget(str(self.segno)+str(self.importo))
        item2=QTableWidget(str(self.descrizione))
        self.tabella.setItem(lastrow,0,item2)
        self.tabella.setItem(lastrow,1,item)




    #Questa funzione apre un MessageBox di errore per l'inserimento errato dell'importo
    def box_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Formato errato")
        msg.setInformativeText("Inserire l'importo corretto")
        msg.setWindowTitle("Errore Importo")
        msg.setStandardButtons(QMessageBox.Ok)
        result = msg.exec()





