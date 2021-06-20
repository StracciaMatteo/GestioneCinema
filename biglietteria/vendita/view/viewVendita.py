from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from biglietteria.controller.controllerTicket import controllerTicket
from listaFilm.controller.controllerListaFilm import controllerListaFilm


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

        self.vista.table_programmazione.clicked.connect(self.assegna_data)

    # seleziona una proiezione specifica e ne permette la vendita
    def assegna_data(self, item):

        self.vista.btn_inserisci.clicked.connect(self.vendi(item))



        '''
        inserire il comando che collega il bottone genera alla funzione vendi_biglietto del controller
        la funzione vendi_biglietto richiede come parametri self.vista.calendar.selectedDate(), item e la quantità da
        vendere fare in modo che alla pressione del bottone genera vengano letti i contatori per passare alla funzione
        vendi_biglietti le quantità e i parametri, la funzione restituisce una stringa con il codice univoco dello
        spettacolo. Chiamare la funzione save del controller all'interno di go_back per salvare la nuova situazione di
        disponibilità dei posti
        '''

    def vendi(self, item):
        quantita = self.vista.Ridotto.value() + self.vista.Adulto.value() + self.vista.Over60.value()
        self.controller.vendi_biglietto(self.vista.calendar.selectedDate(), item, quantita)


    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)
        self.controller.save()

