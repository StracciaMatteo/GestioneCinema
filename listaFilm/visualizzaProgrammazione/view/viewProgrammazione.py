from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox

from listaFilm.controller.controllerListaFilm import controllerListaFilm
from listaFilm.visualizzaProgrammazione.view.viewFilm import viewFilm
from messaggeError.Error import Error


class viewProgrammazione(QWidget):
    def __init__(self, widget):
        super(viewProgrammazione, self).__init__()
        self.widget = widget

        self.controller = controllerListaFilm()

        self.vista = uic.loadUi("listaFilm/visualizzaProgrammazione/view/ProgrammazioneSpettacoli.ui", self)
        # funzione che assegna al box_elenco_film i film in memoria in ordine alfabetico
        self.popola_box_film()

        self.vista.btn_torna.clicked.connect(self.go_back)

        self.vista.btn_dettagli.clicked.connect(self.show_film)

        self.vista.btn_dialog.accepted.connect(self.save)
        self.vista.btn_dialog.rejected.connect(self.go_back)

        # Interazione con calendario
        self.vista.calendar.clicked.connect(self.get_data)

    # assegna la data dal calendario
    def get_data(self):
        data = self.vista.calendar.selectedDate()
        self.vista.label_data.setText(data.toString('dddd, d MMMM yyyy'))
        self.vista.table_programmazione.doubleClicked.connect(self.assegna_data)

    # assegna spettacolo da tabella
    def assegna_data(self, item):
        self.vista.table_programmazione.setItem(item.row(), item.column(), QTableWidgetItem(str(self.vista.box_elenco_film.currentText())))

    # funzione che apre la vista dettagli di un film sela lista_film non è vuota
    def show_film(self):
        if self.vista.box_elenco_film.currentText() == '':
            error = Error("Memoria film vuota", "Nessun film in memoria", "inserire un film nell'apposita sezione")
            error.error_messagge()
        else:
            vista_dettagli = viewFilm(self.controller.get_film_by_name(self.vista.box_elenco_film.currentText()), self.controller, self.rimuovi_film_dal_box)
            vista_dettagli.show()

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    def save(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    # funzioni per gestire box_elenco_film
    def popola_box_film(self):
        for film in self.controller.get_lista_film():
            self.vista.box_elenco_film.addItem(film.titolo)

    def rimuovi_film_dal_box(self):
        self.vista.box_elenco_film.removeItem(self.vista.box_elenco_film.findText(self.vista.box_elenco_film.currentText()))