
from PyQt5 import uic,QtCore
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import QDate

from dipendente.ListaDipendente.controller.ControllerListaDipendenti import ControllerListaDipendenti





class ViewTurniDiLavoro(QWidget):
    def __init__(self, widget):
        super(ViewTurniDiLavoro, self).__init__()
        self.widget = widget
        self.controllerdip = ControllerListaDipendenti()
        self.vista_turni_lavoro = uic.loadUi("dipendente/DatiDipendente/view/TurniDiLavoro.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.popola_tabella()
        self.calendarWidget.clicked.connect(self.popola_tabella)
        self.tabella.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #self.tabella.itemDoubleClicked.connect(self.edit_session)
        self.tabella.cellClicked.connect(self.edit_session)
        #self.tabella.itemDoubleClicked(self.tabella.currentItem()).connect(self.prova)

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
            #self.vista_turni_lavoro.tabella.setItem(cont, 1, QTableWidgetItem(" "))
            #self.vista_turni_lavoro.tabella.setItem(cont, 2, QTableWidgetItem(" "))
            self.vista_turni_lavoro.tabella.setVerticalHeaderItem(cont, QTableWidgetItem(str(cont + 1) + "." + dipendente.cognome + " " + dipendente.nome))
            a = QtCore.QDate.fromString(dipendente.ferie_dal, "dd/MM/yyyy")
            b = QtCore.QDate.fromString(dipendente.ferie_al, "dd/MM/yyyy")
            c=QtCore.QDate.fromString(data_scelta.split()[1], "dd/MM/yyyy")
            if a<=c and c<=b :
                self.vista_turni_lavoro.tabella.setItem(cont,0,QTableWidgetItem("Ferie dal "+dipendente.ferie_dal+" al "+dipendente.ferie_al))
            else:
                if dipendente.giorno_libero.split()[0]==self.get_giorno(data_scelta.split()[0]) or dipendente.giorno_libero.split()[1]==self.get_giorno(data_scelta.split()[0]):
                    self.vista_turni_lavoro.tabella.setItem(cont, 0, QTableWidgetItem("Giorno Libero"))
                else:
                    self.vista_turni_lavoro.tabella.setItem(cont, 0, QTableWidgetItem(dipendente.turno_lavoro))

            cont+=1

        self.tool_tip()

    def edit_session(self):
        #dip_selec=self.vista_turni_lavoro.tabella.currentItem()
        print(self.vista_turni_lavoro.tabella.currentColumn())
        if  self.vista_turni_lavoro.tabella.currentColumn()==1:
            self.popola_edit_box()

    def popola_edit_box(self):
        self.vista_turni_lavoro.edit_box.addItem("Assente")
        self.vista_turni_lavoro.edit_box.addItem("Assenza Verificata")

    '''def prova(self):
        print("ok")'''
    def get_giorno(self,day):

        switcher={
            "Sun":"Dom",
            "Mon":"Lun",
            "Tue":"Mar",
            "Wed":"Mer",
            "Thu":"Gio",
            "Fri":"Ven",
             "Sat":"Sab"
            }
        return (switcher.get(day))

    def tool_tip(self):
        items=self.vista_turni_lavoro.tabella.findItems(" ", Qt.MatchContains)
        for item in items:
            item.setToolTip(item.text())






    '''def printer(self):
        if "20/07/1999"<"18/6/1998":
            print ("ok")'''