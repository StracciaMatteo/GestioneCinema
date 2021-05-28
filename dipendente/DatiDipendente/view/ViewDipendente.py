from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ViewDipendente(QWidget):
    def __init__(self):
        super(ViewDipendente, self).__init__()
        uic.loadUi("dipendente/DatiDipendente/view/Dipendente.ui",self)

