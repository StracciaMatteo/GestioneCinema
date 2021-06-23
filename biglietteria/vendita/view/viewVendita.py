from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from biglietteria.controller.controllerTicket import controllerTicket
from listaFilm.controller.controllerListaFilm import controllerListaFilm
from messaggeError.Error import Error


class viewVendita(QWidget):
    def __init__(self, widget):
        super(viewVendita, self).__init__()
        self.widget = widget
        #self.controller = controllerTicket()
        self.controller = controllerListaFilm()
        self.vista = uic.loadUi("biglietteria/vendita/view/venditabiglietti.ui",self)

        # impostazione parametri calendarWidget per evitare selezioni di date lontane
        today = QDate.currentDate()
        self.vista.calendar.setDateRange(today.addDays(-7), today.addMonths(1))

        # bottone indietro
        self.vista.btn_torna.clicked.connect(self.go_back)

        # Interazione con calendario
        self.vista.calendar.clicked.connect(self.get_data)

    # assegna la data dal calendario e legge programmazione desiderata
    def get_data(self):
        data = self.vista.calendar.selectedDate()
        self.vista.label_data.setText(data.toString('dddd, d MMMM yyyy'))

        # NEW legge la programmazione del json della data attuale
        self.controller.leggi(data.toString('d MMMM yyyy'), self.vista)

        self.vista.btn_inserisci.clicked.connect(self.vendi)

    def vendi(self):
        row = self.vista.table_programmazione.currentRow()
        column = self.vista.table_programmazione.currentColumn()
        item = self.vista.table_programmazione.item(row, column)
        quantita = self.vista.Ridotto.value() + self.vista.Adulto.value() + self.vista.Over60.value()
        self.controller.vendi_biglietto(self.vista.calendar.selectedDate(), item, quantita)
        self.controller.save()

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)
        self.controller.save()

