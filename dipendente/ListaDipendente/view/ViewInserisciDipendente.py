
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from dipendente.DatiDipendente.model.DipendenteModel import DipendenteModel
from dipendente.ListaDipendente.controller.ControllerListaDipendenti import ControllerListaDipendenti
import time

class ViewInserisciDipendente(QWidget):
    def __init__(self, widget,controllerdip,callback,casa):
        super(ViewInserisciDipendente, self).__init__()
        self.widget = widget
        self.callback=callback
        self.controllerdip = controllerdip
        self.casa=casa
        self.vista_inserisci_dipendente = uic.loadUi("dipendente/ListaDipendente/view/InserisciDipendente.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.btn_inserisci_dip.clicked.connect(self.verifica_dati)
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_inserisci_dipendente)
    def go_home(self):
        self.widget.setCurrentIndex(1)
        self.widget.removeWidget(self.vista_inserisci_dipendente)
        self.casa()
    def get_dati_dipendente(self):
        nomedip = self.vista_inserisci_dipendente.Nome.text()
        cognomedip = self.vista_inserisci_dipendente.cognome.text()
        luogo = self.vista_inserisci_dipendente.Luogo_di_nascita.text()
        cf = self.vista_inserisci_dipendente.Codice_fiscale.text()
        stipendiodip = self.vista_inserisci_dipendente.Stipendio.text()
        commentodip = self.vista_inserisci_dipendente.Commento.toPlainText()
        sesso = self.vista_inserisci_dipendente.Sesso.currentText()
        mansione = self.vista_inserisci_dipendente.Mansione.currentText()
        qdata = self.vista_inserisci_dipendente.Data_di_nascita.date()
        data = qdata.toString("dd/MM/yyyy")
        ts=str(time.time())
        id=cognomedip[:2]+nomedip[:2]+data[-2:]+ts[8:10]+cf[-2:]
        gl=self.giorni_liberi()
        modello = DipendenteModel(nomedip, cognomedip, sesso, data, luogo, mansione, cf, stipendiodip, id, self.turno_di_lavoro(),
                                  gl[0]+" "+gl[1], "null", "null", commentodip)
        return modello


    def save_new_dipendente(self):
        modello=self.get_dati_dipendente()
        self.controllerdip.aggiungi_dipendente(modello)
        self.controllerdip.save()
        self.callback(modello)
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_inserisci_dipendente)

    def verifica_dati(self):
        if self.vista_inserisci_dipendente.Nome.text()=="" or self.vista_inserisci_dipendente.cognome.text()=="" or self.vista_inserisci_dipendente.Luogo_di_nascita.text()=="" or self.vista_inserisci_dipendente.Codice_fiscale.text()=="" or self.vista_inserisci_dipendente.Stipendio.text()=="":
            self.vista_inserisci_dipendente.error.setText("i dati sono mancanti")
        else:
            self.save_new_dipendente()
    def turno_di_lavoro(self):

        if len(self.controllerdip.modeldip.listdipendent)==0:
            return "primo turno"
        else:
            contp=0
            conts=0
            for dipendente in self.controllerdip.modeldip.listdipendent:
                if dipendente.turno_lavoro=="primo turno":
                   contp+=1
                else:
                    conts+=1
            if conts<contp:
                return "secondo turno"
            else:
                return "primo turno"

    def giorni_liberi(self):
        giorni=["Lun","Mar","Mer","Gio","Ven","Sab","Dom"]
        giorniscelti=[]
        if len(self.controllerdip.modeldip.listdipendent) == 0:
            giorniscelti.append(giorni[0])
            giorniscelti.append(giorni[1])
            return giorniscelti
        else:
            if self.controllerdip.modeldip.listdipendent[len(self.controllerdip.modeldip.listdipendent)-1].giorno_libero.split()[1]=="Mar":
                giorniscelti.append(giorni[1])
                giorniscelti.append(giorni[2])
                return giorniscelti
            if self.controllerdip.modeldip.listdipendent[len(self.controllerdip.modeldip.listdipendent)-1].giorno_libero.split()[1]=="Mer":
                giorniscelti.append(giorni[2])
                giorniscelti.append(giorni[3])
                return giorniscelti
            if self.controllerdip.modeldip.listdipendent[len(self.controllerdip.modeldip.listdipendent)-1].giorno_libero.split()[1]=="Gio":
                giorniscelti.append(giorni[3])
                giorniscelti.append(giorni[4])
                return giorniscelti
            if self.controllerdip.modeldip.listdipendent[len(self.controllerdip.modeldip.listdipendent)-1].giorno_libero.split()[1]=="Ven":
                giorniscelti.append(giorni[4])
                giorniscelti.append(giorni[5])
                return giorniscelti
            if self.controllerdip.modeldip.listdipendent[len(self.controllerdip.modeldip.listdipendent)-1].giorno_libero.split()[1]=="Sab":
                giorniscelti.append(giorni[5])
                giorniscelti.append(giorni[6])
                return giorniscelti
            else:
                giorniscelti.append(giorni[0])
                giorniscelti.append(giorni[1])
                return giorniscelti

