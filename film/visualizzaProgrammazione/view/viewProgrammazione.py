from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class viewProgrammazione(QWidget):
    def __init__(self, widget):
        super(viewProgrammazione, self).__init__()
        self.widget = widget
        self.vista = uic.loadUi("film/visualizzaProgrammazione/view/ProgrammazioneSpettacoli.ui", self)

        self.btn_torna.clicked.connect(self.go_back)

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)
