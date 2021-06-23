from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox

from InserimentoSpeseRicavi.view.VistaInserimentoSpeseRicavi import VistaInserimentoSpeseRicavi
from messaggeError.Error import Error
from spesericavi.controller.CotrolloreListaMovimenti import ControlloreListaMovimenti


class VistaListaMovimenti(QWidget):
    def __init__(self, widget):
        super(VistaListaMovimenti, self).__init__()
        self.widget = widget
        self.vista= uic.loadUi("spesericavi/view/Lista_Movimenti_UI2.ui", self)
        self.controlloremov = ControlloreListaMovimenti()
        self.voci_nella_lista()
        self.btn_torna_LM.clicked.connect(self.go_back)
        self.btn_InserisciMovLM.clicked.connect(self.apri_inserisci_voce)
        self.btn_RimuoviMovLM.clicked.connect(self.elimina_voce)


    # Funzione che permette di accedere alla funzione inserimento voce
    def apri_inserisci_voce(self):
        inserisci_voce = VistaInserimentoSpeseRicavi(self.widget)
        self.widget.addWidget(inserisci_voce)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
    # Funizone che permette di tornare inditro con il tasto "<-"
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    def voci_nella_lista(self):
        cont=0
        for voci in self.controlloremov.modellist.listamovimenti:
            item= self.vista.lista_voci.takeItem(cont)
            cont +=1
        self.vista.lista_voci.setSortingEnabled(False)
        for voci in self.controlloremov.modellist.listamovimenti:
            self.vista.lista_voci.addItem(voci.segno+voci.importo+"  "+voci.descrizione)

    def box_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Selezione una voce")
        msg.setWindowTitle("Errore")
        msg.setStandardButtons(QMessageBox.Ok)
        result = msg.exec()

    #-----------------------------------------------------------
    def elimina_voce(self):
        if self.vista.lista_voci.currentRow()==-1:
            self.vista.error.setText("Nessuna voce è stata selezionata")
        else:
            self.box_dialog()

    def box_dialog(self):
        error = Error("Attenzione","Vuoi eliminare la voce ?","")
        if error.confirm_messagge() == QMessageBox.Yes:
            item = self.vista.lista_voci.takeItem(
                self.vista.lista_voci.currentRow())
            descrizione = item.text()
            self.controlloremov.rimuovi_voce(descrizione.split()[0])
            self.controlloremov.save()
