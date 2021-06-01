from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox


class viewFilm(QWidget):
    def __init__(self, film, controller):
        super(viewFilm, self).__init__()
        self.film = film
        self.controller = controller
        self.vista = uic.loadUi("listaFilm/visualizzaProgrammazione/view/DettagliFilm.ui", self)
        self.vista.Titolo.setText(self.film.titolo)
        self.vista.label_durata.setText("Durata: "+film.durata.toString())
        self.vista.label_intervallo.setText("Inizio intervallo: " + film.intervallo.toString())

        self.vista.btn_elimina_film.clicked.connect(self.box_dialog)

    def box_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Eliminare definitivamente ?")
        msg.setInformativeText("L'operazione è irreversibile")
        msg.setWindowTitle("Elimina film")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        result = msg.exec()
        if result == QMessageBox.Yes:
            self.controller.rimuovi(self.film)
            self.controller.save()
        self.vista.close()
