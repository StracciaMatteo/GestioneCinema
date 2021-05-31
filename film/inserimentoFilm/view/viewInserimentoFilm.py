from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class viewInserimentoFilm(QWidget):
    def __init__(self, widget):
        super(viewInserimentoFilm, self).__init__()
        self.widget = widget
        self.vista = uic.loadUi("film/inserimentoFilm/view/InserisciFilm.ui", self)
