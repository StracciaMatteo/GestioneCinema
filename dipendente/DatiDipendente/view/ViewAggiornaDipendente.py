from PyQt5 import uic,QtCore, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget

from dipendente.ListaDipendente.controller.ControllerListaDipendenti import ControllerListaDipendenti
from messaggeError.Error import Error


class ViewAggiornaDipendente(QWidget):
    def __init__(self, widget,dipendente,controllerdip,callback,lista):
        super(ViewAggiornaDipendente, self).__init__()
        self.widget = widget
        self.dipendente = dipendente
        self.callback=callback
        self.lista=lista
        self.controllerdip= controllerdip
        self.vista_aggiorna_dipendente = uic.loadUi("dipendente/DatiDipendente/view/AggiornaDipendente.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.visualizza_dipendente(dipendente)
        self.ferie_on.clicked.connect(self.enable_ferie)
        self.vista_aggiorna_dipendente.Ferie_dal.setDisabled(True)
        self.vista_aggiorna_dipendente.Ferie_al_1.setDisabled(True)
        self.vista_aggiorna_dipendente.salva_modifica.clicked.connect(self.update_dip)
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_aggiorna_dipendente)

    def go_home(self):
        self.widget.setCurrentIndex(1)
        self.widget.removeWidget(self.vista_aggiorna_dipendente)

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


    def leggi_ferie(self,ferie_dal,ferie_al):
        if ferie_dal=="null" and ferie_al=="null":
            self.vista_aggiorna_dipendente.Ferie_dal.setDate(QDate.currentDate())
            self.vista_aggiorna_dipendente.Ferie_al_1.setDate(QDate.currentDate())
        else:
            self.vista_aggiorna_dipendente.Ferie_dal.setDate(QtCore.QDate.fromString(ferie_dal, "dd/MM/yyyy"))
            self.vista_aggiorna_dipendente.Ferie_al_1.setDate(QtCore.QDate.fromString(ferie_al, "dd/MM/yyyy"))

    def scrivi_ferie(self):
       if self.vista_aggiorna_dipendente.ferie_on.isChecked():
           dal_data = self.vista_aggiorna_dipendente.Ferie_dal.date()
           al_data = self.vista_aggiorna_dipendente.Ferie_al_1.date()
           self.dipendente.ferie_dal = dal_data.toString("dd/MM/yyyy")
           self.dipendente.ferie_al = al_data.toString("dd/MM/yyyy")


    def enable_ferie(self):
       if self.vista_aggiorna_dipendente.ferie_on.isChecked():
           self.vista_aggiorna_dipendente.Ferie_dal.setDisabled(False)
           self.vista_aggiorna_dipendente.Ferie_al_1.setDisabled(False)
       else:
           self.vista_aggiorna_dipendente.Ferie_dal.setDisabled(True)
           self.vista_aggiorna_dipendente.Ferie_al_1.setDisabled(True)

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
        self.go_back()
    def box_dialog_upadate(self):
        error = Error("Aggiornamento Dipendente", "Le modifiche sono state salvate correttamente.", "")
        error.information_message()


