from PyQt5 import uic
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QColor, QBrush, QIcon
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QMessageBox

from dipendente.DatiDipendente.view.ViewAggiornaDipendente import ViewAggiornaDipendente
from dipendente.DatiDipendente.view.ViewDipendente import ViewDipendente
from dipendente.ListaDipendente.controller.ControllerListaDipendenti import ControllerListaDipendenti
from dipendente.ListaDipendente.view.ViewInserisciDipendente import ViewInserisciDipendente
from messaggeError.Error import Error


class ViewListaDipendente(QWidget):
    def __init__(self, widget):
        super(ViewListaDipendente, self).__init__()
        self.widget = widget
        self.controllerdip = ControllerListaDipendenti()
        self.vista_lista_dipendente = uic.loadUi("dipendente/ListaDipendente/view/ListaDipendenti.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.btn_inserisci_dip.clicked.connect(self.go_inserisci_dipendente)
        self.btn_ricerca.clicked.connect(self.search_dipendente)
        self.btn_elimina_dip.clicked.connect(self.remove_dipendente)
        self.btn_aggiorna_dip.clicked.connect(self.go_aggiorna_dipendente)
        self.popola_lista_dipententi()
        self.list_dipendenti.itemDoubleClicked.connect(self.go_view_dipendente)

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_lista_dipendente)

    def go_home(self):
        self.widget.setCurrentIndex(1)
        self.widget.removeWidget(self.vista_lista_dipendente)

    def go_to(self, vista):
        self.widget.addWidget(vista)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        vista.btn_Home.clicked.connect(self.go_home)

    def go_inserisci_dipendente(self):
        vista_inseriscidipendente = ViewInserisciDipendente(self.widget,self.controllerdip,self.add_dipendente)
        self.go_to(vista_inseriscidipendente)

    def go_aggiorna_dipendente(self):
        if self.vista_lista_dipendente.list_dipendenti.currentRow()==-1:
            self.vista_lista_dipendente.error.setText("Nessun dipendente e' stato selezionato")
        else:
            cognome = self.vista_lista_dipendente.list_dipendenti.currentItem().text()
            dipendente = self.controllerdip.get_dipendente_by_name(cognome.split()[-1],cognome.split()[0])
            item = self.vista_lista_dipendente.list_dipendenti.takeItem(self.vista_lista_dipendente.list_dipendenti.currentRow())
            vista_aggiornadipendente=ViewAggiornaDipendente(self.widget,dipendente,self.controllerdip,self.add_dipendente)
            self.go_to(vista_aggiornadipendente)

    def popola_lista_dipententi(self):
        cont=0
        for dipendente in self.controllerdip.modeldip.listdipendent:
            item = self.vista_lista_dipendente.list_dipendenti.takeItem(cont)
            cont+=1
        self.vista_lista_dipendente.list_dipendenti.setSortingEnabled(True)
        for dipendente in self.controllerdip.modeldip.listdipendent:
            self.vista_lista_dipendente.list_dipendenti.addItem(dipendente.cognome + " " + dipendente.nome)
        self.add_icon()

    def go_view_dipendente(self):
        cognome=self.vista_lista_dipendente.list_dipendenti.currentItem().text()
        dipendente=self.controllerdip.get_dipendente_by_name(cognome.split()[-1],cognome.split()[0])
        viewdipendente=ViewDipendente(self.widget,dipendente,self.remove_dipendente)
        self.go_to(viewdipendente)

    def search_dipendente(self):
        if self.vista_lista_dipendente.barra_ricerca.text()=="":
            self.vista_lista_dipendente.error.setText("La barra di ricerca e' vuota")
        else:
            self.vista_lista_dipendente.error.setText("")
            self.vista_lista_dipendente.list_dipendenti.setSortingEnabled(False)
            cont=0
            for dipendente in self.controllerdip.modeldip.listdipendent:
                searcheditem = self.vista_lista_dipendente.list_dipendenti.item(cont)
                searcheditem.setBackground(QColor(255,255, 255,255))
                cont+=1
            items=self.vista_lista_dipendente.list_dipendenti.findItems(self.vista_lista_dipendente.barra_ricerca.text(),Qt.MatchContains)
            if items==[]:
                self.vista_lista_dipendente.error.setText("Non e' stato torvato nessun dipendente")
            else:
                for item in items:
                    dip=self.vista_lista_dipendente.list_dipendenti.takeItem(self.vista_lista_dipendente.list_dipendenti.row(item))
                    self.vista_lista_dipendente.list_dipendenti.insertItem(0,dip.text())
                    searchitem=self.vista_lista_dipendente.list_dipendenti.item(0)
                    searchitem.setBackground(QColor(0,242,255,255))
                    icon = QIcon()
                    icon.addFile("images/Dipendente-Icon.png", QSize(), QIcon.Normal, QIcon.Off)
                    item = self.vista_lista_dipendente.list_dipendenti.item(0)
                    item.setIcon(icon)

    def remove_dipendente(self):
        if self.vista_lista_dipendente.list_dipendenti.currentRow()==-1:
            self.vista_lista_dipendente.error.setText("Nessun dipendente e' stato selezionato")
        else:
            self.vista_lista_dipendente.error.setText("")
            self.box_dialog()

    def add_icon(self):
        cont=0
        for dipendente in self.controllerdip.modeldip.listdipendent:
            icon=QIcon()
            icon.addFile("images/Dipendente-Icon.png",QSize(),QIcon.Normal,QIcon.Off)
            item = self.vista_lista_dipendente.list_dipendenti.item(cont)
            item.setIcon(icon)
            cont+=1

    def box_dialog(self):
        error = Error("Elimina dipendente", "Eliminare definitivamente ?", "L'operazione è irreversibile")
        if error.confirm_messagge() == QMessageBox.Yes:
            item = self.vista_lista_dipendente.list_dipendenti.takeItem(
                self.vista_lista_dipendente.list_dipendenti.currentRow())
            cognome = item.text()
            self.controllerdip.remove_dipendente_by_name(cognome.split()[-1],cognome.split()[0])
            self.controllerdip.save()

    def add_dipendente(self,modello):
        self.vista_lista_dipendente.list_dipendenti.addItem(modello.cognome+" "+modello.nome)
        items = self.vista_lista_dipendente.list_dipendenti.findItems(modello.cognome,Qt.MatchContains)
        for item in items:
            icon = QIcon()
            icon.addFile("images/Dipendente-Icon.png", QSize(), QIcon.Normal, QIcon.Off)
            item.setIcon(icon)
