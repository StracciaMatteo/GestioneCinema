from PyQt5 import uic,QtCore, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QMessageBox

from dipendente.ListaDipendente.controller.ControllerListaDipendenti import ControllerListaDipendenti
from messaggeError.Error import Error
#Classe che si occupa della visualizzazione di vista Aggiorna dipendente

class ViewAggiornaDipendente(QWidget):
    #Costruttore della vista che prende come parametri:
    #Widget: widget principale
    #dipendente: il dipendente da aggiornare
    #controllerdip: controllore lista dipendente
    #callback:per aggiornare widget lista dipendenti
    #casa: per tornare nella vista Home

    def __init__(self, widget,dipendente,controllerdip,callback,lista,casa):
        super(ViewAggiornaDipendente, self).__init__()
        self.widget = widget
        self.dipendente = dipendente
        self.callback=callback
        self.lista=lista
        self.casa=casa
        self.controllerdip= controllerdip
        self.vista_aggiorna_dipendente = uic.loadUi("dipendente/DatiDipendente/view/AggiornaDipendente.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.visualizza_dipendente(dipendente)
        self.ferie_on.clicked.connect(self.enable_ferie)
        self.vista_aggiorna_dipendente.Ferie_dal.setDisabled(True)
        self.vista_aggiorna_dipendente.Ferie_al_1.setDisabled(True)
        self.vista_aggiorna_dipendente.salva_modifica.clicked.connect(self.verifica_dati_aggiorna)


# metodo per tornare in dietro

    def go_back(self):
        self.verifica_modifica(True)

# metodo per tornare alla vista Home

    def go_home(self):
        self.verifica_modifica(False)

# metodo per popolare labels e ComboBox con i dati del dipendente da aggiornare

    def visualizza_dipendente(self,dipendente):
        self.vista_aggiorna_dipendente.Nome.setText(dipendente.nome)
        self.vista_aggiorna_dipendente.Cognome.setText(dipendente.cognome)
        self.vista_aggiorna_dipendente.Sesso.setCurrentText(dipendente.sesso)
        self.vista_aggiorna_dipendente.Data_di_nascita.setDate(QtCore.QDate.fromString(dipendente.data_nascita,"dd/MM/yyyy"))
        self.vista_aggiorna_dipendente.Luogo_di_nascita.setText(dipendente.luogo_nascita)
        self.vista_aggiorna_dipendente.Mansione.setCurrentText(dipendente.mansione)
        self.vista_aggiorna_dipendente.Codice_fiscale.setText(dipendente.cf)
        self.vista_aggiorna_dipendente.Stipendio.setText(dipendente.stipendio)
        self.vista_aggiorna_dipendente.ID.setText(dipendente.id)
        self.vista_aggiorna_dipendente.Turno_di_lavoro.setCurrentText(dipendente.turno_lavoro)
        self.vista_aggiorna_dipendente.Giorno_libero_1.setCurrentText(dipendente.giorno_libero.split()[0])
        self.vista_aggiorna_dipendente.Giorno_libero_2.setCurrentText(dipendente.giorno_libero.split()[1])
        self.leggi_ferie(dipendente.ferie_dal,dipendente.ferie_al)
        self.vista_aggiorna_dipendente.Commento.setText(dipendente.commento)

    #metodo per popolare QdateEdit che prende come parametri
    #ferie_dal: inizio ferie
    #ferie_al: fine ferie

    def leggi_ferie(self,ferie_dal,ferie_al):
        if ferie_dal=="null" and ferie_al=="null":
            self.vista_aggiorna_dipendente.Ferie_dal.setDate(QDate.currentDate())
            self.vista_aggiorna_dipendente.Ferie_al_1.setDate(QDate.currentDate())
        else:
            self.vista_aggiorna_dipendente.Ferie_dal.setDate(QtCore.QDate.fromString(ferie_dal, "dd/MM/yyyy"))
            self.vista_aggiorna_dipendente.Ferie_al_1.setDate(QtCore.QDate.fromString(ferie_al, "dd/MM/yyyy"))

    #metodo per aggionrare i dati del dipendente dal QdateEdit

    def scrivi_ferie(self):
       if self.vista_aggiorna_dipendente.ferie_on.isChecked():
           dal_data = self.vista_aggiorna_dipendente.Ferie_dal.date()
           al_data = self.vista_aggiorna_dipendente.Ferie_al_1.date()
           self.dipendente.ferie_dal = dal_data.toString("dd/MM/yyyy")
           self.dipendente.ferie_al = al_data.toString("dd/MM/yyyy")

    #metodo per mettere in funzione le QdateEdit una volta vine spuntate la checkbox dal utente

    def enable_ferie(self):
       if self.vista_aggiorna_dipendente.ferie_on.isChecked():
           self.vista_aggiorna_dipendente.Ferie_dal.setDisabled(False)
           self.vista_aggiorna_dipendente.Ferie_al_1.setDisabled(False)
       else:
           self.vista_aggiorna_dipendente.Ferie_dal.setDisabled(True)
           self.vista_aggiorna_dipendente.Ferie_al_1.setDisabled(True)

    #metodo per aggionrare i dati inseriti dal utente

    def update_dip(self):
        self.dipendente.nome= self.vista_aggiorna_dipendente.Nome.text()
        self.dipendente.cognome= self.vista_aggiorna_dipendente.Cognome.text()
        self.dipendente.luogo_nascita= self.vista_aggiorna_dipendente.Luogo_di_nascita.text()
        self.dipendente.cf = self.vista_aggiorna_dipendente.Codice_fiscale.text()
        self.dipendente.stipendio= self.vista_aggiorna_dipendente.Stipendio.text()
        self.dipendente.commento= self.vista_aggiorna_dipendente.Commento.toPlainText()
        self.dipendente.sesso= self.vista_aggiorna_dipendente.Sesso.currentText()
        self.dipendente.mansione=self.vista_aggiorna_dipendente.Mansione.currentText()
        qdata = self.vista_aggiorna_dipendente.Data_di_nascita.date()
        self.dipendente.data_nascita=qdata.toString("dd/MM/yyyy")
        self.dipendente.id=self.vista_aggiorna_dipendente.ID.text()
        self.dipendente.turno_lavoro=self.vista_aggiorna_dipendente.Turno_di_lavoro.currentText()
        libero_1=self.vista_aggiorna_dipendente.Giorno_libero_1.currentText()
        libero_2=self.vista_aggiorna_dipendente.Giorno_libero_2.currentText()
        self.dipendente.giorno_libero=libero_1+" "+libero_2
        self.scrivi_ferie()
        self.controllerdip.save()
        self.lista.list_dipendenti.takeItem(self.lista.list_dipendenti.currentRow())
        self.callback(self.dipendente)
        self.box_dialog_upadate()
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_aggiorna_dipendente)

    #metodo per visulazziare QMassegeBox per confermare il salvataggio delle modifche

    def box_dialog_upadate(self):
        error = Error("Aggiornamento Dipendente", "Le modifiche sono state salvate correttamente.", "")
        error.information_message()
    #metodo che viene eseguito una volta che l'utene esce dalla vista senza cliccare sul bottone "salva modifiche" e prende come parametri:
    #bool: gli viene passato il valore True in caso l'utene clicca sul bottone "torna indietro" e False in caso l'utente clicca sul  bottone "Home"
    def box_dialog_modifica (self,bool):
        error = Error("Aggiornamento Dipendente", "Le modifiche non sono state salvate.", "Vorresti salvarle?")
        if error.confirm_messagge() == QMessageBox.Yes:
            self.update_dip()
        else:
            if bool:
                self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
                self.widget.removeWidget(self.vista_aggiorna_dipendente)
            else:
                self.widget.setCurrentIndex(1)
                self.widget.removeWidget(self.vista_aggiorna_dipendente)
                self.casa()

    #metodo per verificare i dati inseriti dal'utente

    def verifica_dati_aggiorna(self):
        if self.vista_aggiorna_dipendente.ID.text()=="" or self.vista_aggiorna_dipendente.Nome.text()=="" or self.vista_aggiorna_dipendente.Cognome.text()=="" or self.vista_aggiorna_dipendente.Luogo_di_nascita.text()=="" or self.vista_aggiorna_dipendente.Codice_fiscale.text()=="" or self.vista_aggiorna_dipendente.Stipendio.text()=="":
            self.vista_aggiorna_dipendente.error_text.setText("i dati sono mancanti")
        else:
            if self.vista_aggiorna_dipendente.Ferie_dal.date() > self.vista_aggiorna_dipendente.Ferie_al_1.date():
                self.vista_aggiorna_dipendente.error_text.setText("La data di inizio ferie supera quella di fine ferie")
            else:
                self.update_dip()

    def verifica_modifica(self,bool):
        if self.vista_aggiorna_dipendente.ID.text()=="" or self.vista_aggiorna_dipendente.Nome.text()=="" or self.vista_aggiorna_dipendente.Cognome.text()=="" or self.vista_aggiorna_dipendente.Luogo_di_nascita.text()=="" or self.vista_aggiorna_dipendente.Codice_fiscale.text()=="" or self.vista_aggiorna_dipendente.Stipendio.text()=="":
            self.vista_aggiorna_dipendente.error_text.setText("i dati sono mancanti")
        else:
            if self.vista_aggiorna_dipendente.Ferie_dal.date() > self.vista_aggiorna_dipendente.Ferie_al_1.date():
                self.vista_aggiorna_dipendente.error_text.setText("La data di inizio ferie supera quella di fine ferie")
            else:
                libero_1 = self.vista_aggiorna_dipendente.Giorno_libero_1.currentText()
                libero_2 = self.vista_aggiorna_dipendente.Giorno_libero_2.currentText()
                if self.dipendente.nome== self.vista_aggiorna_dipendente.Nome.text() and self.dipendente.cognome==self.vista_aggiorna_dipendente.Cognome.text() and self.dipendente.luogo_nascita== self.vista_aggiorna_dipendente.Luogo_di_nascita.text() and self.dipendente.cf == self.vista_aggiorna_dipendente.Codice_fiscale.text() and self.dipendente.stipendio== self.vista_aggiorna_dipendente.Stipendio.text() and self.dipendente.commento== self.vista_aggiorna_dipendente.Commento.toPlainText() and self.dipendente.sesso== self.vista_aggiorna_dipendente.Sesso.currentText() and self.dipendente.mansione==self.vista_aggiorna_dipendente.Mansione.currentText() and self.dipendente.data_nascita==self.vista_aggiorna_dipendente.Data_di_nascita.date().toString("dd/MM/yyyy") and self.dipendente.id==self.vista_aggiorna_dipendente.ID.text() and self.dipendente.turno_lavoro==self.vista_aggiorna_dipendente.Turno_di_lavoro.currentText() and self.dipendente.giorno_libero==libero_1+" "+libero_2  and not self.vista_aggiorna_dipendente.ferie_on.isChecked():
                   if bool:
                       self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
                       self.widget.removeWidget(self.vista_aggiorna_dipendente)
                   else:
                       self.widget.setCurrentIndex(1)
                       self.widget.removeWidget(self.vista_aggiorna_dipendente)
                       self.casa()
                else:
                    self.box_dialog_modifica(bool)