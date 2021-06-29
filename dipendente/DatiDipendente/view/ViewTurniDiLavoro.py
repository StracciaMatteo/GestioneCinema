from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class ViewTurniDiLavoro(QWidget):
    def __init__(self, widget):
        super(ViewTurniDiLavoro, self).__init__()
        self.widget = widget
        self.vista_turni_lavoro = uic.loadUi("dipendente/DatiDipendente/view/TurniDiLavoro.ui",self)
        self.btn_torna.clicked.connect(self.go_back)
        self.btn_Home.clicked.connect(self.go_home)
        self.calendarWidget.clicked.connect(self.date)
    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista_turni_lavoro)

    def go_home(self):
        self.widget.setCurrentIndex(1)
        self.widget.removeWidget(self.vista_turni_lavoro)
    def date(self):
        print(self.vista_turni_lavoro.calendarWidget.selectedDate().toString("dd/MM/yyyy"))
        print(str(self.vista_turni_lavoro.calendarWidget.firstDayOfWeek()))
