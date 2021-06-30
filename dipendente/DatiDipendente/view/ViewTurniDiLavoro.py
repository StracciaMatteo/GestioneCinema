from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from dipendente.ListaDipendente.controller.ControllerListaDipendenti import ControllerListaDipendenti


class ViewTurniDiLavoro(QWidget):
    def __init__(self, widget):
        super(ViewTurniDiLavoro, self).__init__()
        self.widget = widget
        self.controllerdip = ControllerListaDipendenti()
        self.vista_turni_lavoro = uic.loadUi("dipendente/DatiDipendente/view/TurniDiLavoro.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.calendarWidget.clicked.connect(self.popola_tabella)
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_turni_lavoro)

    def go_home(self):
        self.widget.setCurrentIndex(1)
        self.widget.removeWidget(self.vista_turni_lavoro)
    def popola_tabella(self):
        data_scelta=self.vista_turni_lavoro.calendarWidget.selectedDate().toString("ddd dd/MM/yyyy")
        self.vista_turni_lavoro.tabella.setRowCount(len(self.controllerdip.modeldip.listdipendent))
        cont=0
        for dipendente in self.controllerdip.modeldip.listdipendent:
            self.vista_turni_lavoro.tabella.setVerticalHeaderItem(cont,QTableWidgetItem(str(cont+1)+"."+dipendente.cognome + " " + dipendente.nome))
            self.vista_turni_lavoro.tabella.setItem(cont,0,QTableWidgetItem(dipendente.turno_lavoro))
            cont+=1