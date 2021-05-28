from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ViewDipendente(QWidget):
    def __init__(self, widget):
        super(ViewDipendente, self).__init__()
        self.widget = widget
        self.vista_dipendente = uic.loadUi("dipendente/DatiDipendente/view/Dipendente.ui",self)
        self.btn_torna.clicked.connect(self.go_back)

    def go_back(self):
        # print(len(self.widget))
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_dipendente)