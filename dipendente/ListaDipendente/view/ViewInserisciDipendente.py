from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from dipendente.DatiDipendente.model.DipendenteModel import DipendenteModel
from dipendente.ListaDipendente.controller.ControllerListaDipendenti import ControllerListaDipendenti
from dipendente.ListaDipendente.model.ListaDipendenti import ListaDipendenti


class ViewInserisciDipendente(QWidget):
    def __init__(self, widget):
        super(ViewInserisciDipendente, self).__init__()
        self.widget = widget
        self.controllerdip = ControllerListaDipendenti()
        self.vista_inserisci_dipendente = uic.loadUi("dipendente/ListaDipendente/view/InserisciDipendente.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.btn_inserisci_dip.clicked.connect(self.save)
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_inserisci_dipendente)
    def go_home(self):
        self.widget.setCurrentIndex(1)
        self.widget.removeWidget(self.vista_inserisci_dipendente)

    def get_dati_dipendente(self):
        nomedip=self.vista_inserisci_dipendente.Nome.text()
        cognomedip=self.vista_inserisci_dipendente.cognome.text()
        luogo=self.vista_inserisci_dipendente.Luogo_di_nascita.text()
        cf=self.vista_inserisci_dipendente.Codice_fiscale.text()
        stipendiodip=self.vista_inserisci_dipendente.Stipendio.text()
        commentodip=self.vista_inserisci_dipendente.Commento.toPlainText()
        sesso=self.vista_inserisci_dipendente.Sesso.currentIndex()
        mansione=self.vista_inserisci_dipendente.Mansione.currentIndex()
        data=2020
        #qdata=self.vista_inserisci_dipendente.Data_di_nascita.date()
        #data=qdata.toString("dd,MM,yyyy")
        modello=DipendenteModel(nomedip,cognomedip,sesso,data,luogo,mansione,cf,stipendiodip,"null","null","null","null","null",commentodip)
        return modello

    def save(self):

        self.controllerdip.aggiungi_dipendente(self.get_dati_dipendente())
        self.controllerdip.save()
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_inserisci_dipendente)