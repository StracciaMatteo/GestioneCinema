from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox
from messaggeError.Error import Error


class viewFilm(QWidget):
    def __init__(self, film, controller, callback):
        super(viewFilm, self).__init__()
        self.film = film
        self.callback = callback
        self.controller = controller
        self.vista = uic.loadUi("listaFilm/visualizzaProgrammazione/view/DettagliFilm.ui", self)
        self.vista.Titolo.setText(self.film.titolo)
        self.vista.label_durata.setText("Durata: "+film.durata.toString())
        self.vista.label_intervallo.setText("Inizio intervallo: " + film.intervallo.toString())

        self.vista.btn_elimina_film.clicked.connect(self.box_dialog)

    # box che visualizza la conferma di eliminazione
    def box_dialog(self):
        error = Error("Elimina film", "Eliminare definitivamente ?", "L'operazione è irreversibile")
        if error.confirm_messagge() == QMessageBox.Yes:
            self.controller.rimuovi(self.film)
            self.controller.save()
            self.callback()
            self.vista.close()
