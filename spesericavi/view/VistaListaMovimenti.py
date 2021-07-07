from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox

from InserimentoSpeseRicavi.controller.ControlloreInserimentoSR import ControlloreInserimentoSR
from InserimentoSpeseRicavi.view.VistaInserimentoSpeseRicavi import VistaInserimentoSpeseRicavi
from messaggeError.Error import Error
#from spesericavi.controller.CotrolloreListaMovimenti import ControlloreListaMovimenti


class VistaListaMovimenti(QWidget):
    def __init__(self, widget):
        super(VistaListaMovimenti, self).__init__()
        self.widget = widget
        self.vista= uic.loadUi("spesericavi/view/Lista_Movimenti_UI2.ui", self)
        self.controlloremov = ControlloreInserimentoSR()
        self.voci_nella_lista()
        self.totale()
        self.btn_torna_LM.clicked.connect(self.go_back)
        self.btn_InserisciMovLM.clicked.connect(self.apri_inserisci_voce)
        self.btn_RimuoviMovLM.clicked.connect(self.elimina_voce)
        self.btn_RimuoviMovLM.setShortcut("ctrl+r")

    # Funzione che permette di accedere alla vista Inserimento Voce
    def apri_inserisci_voce(self):
        inserisci_voce = VistaInserimentoSpeseRicavi(self.widget,self.vista.lista_voci)
        self.widget.addWidget(inserisci_voce)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    # Funizone che permette di tornare indietro con il tasto "<-" all'interno della vista
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    # Funzione che carica gli elementi prensenti nel file pickle nel List Widget
    def voci_nella_lista(self):
        cont=0
        for voci in self.controlloremov.model.lista_movimenti:
            item= self.vista.lista_voci.takeItem(cont)
            cont +=1
        self.vista.lista_voci.setSortingEnabled(False)
        for voci in self.controlloremov.model.lista_movimenti:
            self.vista.lista_voci.addItem(voci.segno+str(voci.importo)+"  "+voci.descrizione)



    # Funzione che calcola il totale della lista movimenti, oppure in caso di mancato totale stampa nella Line edit il place holder
    def totale(self):
        totale=0
        for voci in self.controlloremov.model.lista_movimenti:
            if voci.segno == "+":
                totale += float(voci.importo)
            else:
                totale -= float(voci.importo)
        if totale != 0 :
            self.vista.lineEdit_Totale.setText(str(totale)+" €")



    # Funzione che crea il message box di errore nel caso non venga selezionata nessuna voce durante l'eliminzaione delle voci
    def box_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Non ci sono piu voci nella lista")
        msg.setWindowTitle("Errore")
        msg.setStandardButtons(QMessageBox.Ok)
        result = msg.exec()

    # Funzione che chiama la funzione di eliminazione della voce se selezionata oppure manda a schermo un Message box di Errore
    def elimina_voce(self):
        if self.vista.lista_voci.currentRow()==-1:
            error = Error("Attenzione", "Voce non selezionata", "")
            error.error_messagge()
        else:
            self.removing_error_box()

    # Funzione che permette di rimuovere la voce dalla lista se si preme "Si" nel Message Box
    def removing_error_box(self):
        error = Error("Attenzione","Vuoi eliminare la voce ?","")
        if error.confirm_messagge() == QMessageBox.Yes:
            descrizione = self.controlloremov.model.lista_movimenti[self.vista.lista_voci.currentRow()].descrizione
            self.vista.lista_voci.takeItem(self.vista.lista_voci.currentRow())
            self.controlloremov.rimuovi_voce(descrizione)
            self.controlloremov.save()


