from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from listaFilm.controller.controllerListaFilm import controllerListaFilm
from listaFilm.visualizzaProgrammazione.view.viewFilm import viewFilm


class viewProgrammazione(QWidget):
    def __init__(self, widget):
        super(viewProgrammazione, self).__init__()
        self.widget = widget

        self.controller = controllerListaFilm()

        self.vista = uic.loadUi("listaFilm/visualizzaProgrammazione/view/ProgrammazioneSpettacoli.ui", self)
        # funzione che assegna al box_elenco_film i film in memoria in ordine alfabetico
        for film in self.controller.get_lista_film():
            self.vista.box_elenco_film.addItem(film.titolo)

        self.vista.btn_torna.clicked.connect(self.go_back)

        self.vista.btn_dettagli.clicked.connect(self.show_film)

        self.vista.btn_dialog.accepted.connect(self.save)
        self.vista.btn_dialog.rejected.connect(self.go_back)

        # Interazione con calendario
        self.vista.calendar.clicked.connect(self.get_data)

    def get_data(self):
        data = self.vista.calendar.selectedDate()
        self.vista.label_data.setText(data.toString('dddd, d MMMM yyyy'))
        self.vista.table_programmazione.doubleClicked.connect(self.assegna_data)

    def assegna_data(self, item):
        self.vista.table_programmazione.setItem(item.row(), item.column(), QTableWidgetItem(str(self.vista.box_elenco_film.currentText())))

    def show_film(self):
        vista_dettagli = viewFilm(self.controller.get_film_by_name(self.vista.box_elenco_film.currentText()), self.controller)
        vista_dettagli.show()

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    def save(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)
