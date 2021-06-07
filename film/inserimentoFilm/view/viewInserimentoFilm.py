from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidget, QPushButton, QTableWidgetItem

from film.model.film import film
from listaFilm.controller.controllerListaFilm import controllerListaFilm
from messaggeError.Error import Error


class viewInserimentoFilm(QWidget):
    def __init__(self, widget):
        super(viewInserimentoFilm, self).__init__()
        self.widget = widget

        self.controller = controllerListaFilm()

        self.vista = uic.loadUi("film/inserimentoFilm/view/InserisciFilm.ui", self)

        # bottoni fondo pagina
        self.vista.btn_dialog.accepted.connect(self.save)
        self.vista.btn_dialog.rejected.connect(self.go_back)

        # Interazione con calendario
        self.vista.calendar.clicked.connect(self.get_data)

    # assegna la data dal calendario
    def get_data(self):
        data = self.vista.calendar.selectedDate()
        self.vista.label_data.setText(data.toString('dddd, d MMMM yyyy'))
        # NEW legge la programmazione del json della data attuale
        self.controller.leggi(data.toString('d MMMM yyyy'), self.vista)
        self.vista.table_programmazione.doubleClicked.connect(self.assegna_data)

    # assegna spettacolo da tabella
    def assegna_data(self, item):
        data = self.vista.calendar.selectedDate()
        durata = self.vista.timeEdit_durata.time()
        # controlla che tutti i campi siano inseriti ed assegna lo spettacolo
        if self.vista.filmName.text() != '' and durata.hour() < 3 and durata.hour() or durata.minute():
            self.vista.table_programmazione.setItem(item.row(), item.column(),
                                                    QTableWidgetItem(str(self.vista.filmName.text())))
            # NEW sostituisce il film selezionato nella variabile ma non nel json
            self.controller.aggiorna_programmazione(data.toString('d MMMM yyyy'),
                                                    str(self.vista.filmName.text()), item)

    def save(self):
        durata = self.vista.timeEdit_durata.time()
        if self.vista.filmName.text() != '' and durata.hour() < 3 and durata.hour() or durata.minute():
            self.controller.aggiungi_film(film(self.vista.filmName.text(), self.vista.timeEdit_durata.time(),
                                               self.vista.timeEdit_intervallo.time()))
            self.controller.save()

            self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
            self.widget.removeWidget(self.vista)
        else:
            error = Error("Dati errati", "Assicurati di aver inserito un titolo e dati corretti",
                          "La durata deve essere compresa fra 1 minuto e 2 ore e 59 minuti")
            error.error_messagge()

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)
