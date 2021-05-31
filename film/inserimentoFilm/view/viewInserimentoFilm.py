from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QTableWidget, QPushButton, QTableWidgetItem


class viewInserimentoFilm(QWidget):
    def __init__(self, widget):
        super(viewInserimentoFilm, self).__init__()
        self.widget = widget
        self.vista = uic.loadUi("film/inserimentoFilm/view/InserisciFilm.ui", self)

        self.vista.btn_dialog.accepted.connect(self.save)
        self.vista.btn_dialog.rejected.connect(self.go_back)

        # Interazione con calendario
        self.vista.calendar.clicked.connect(self.get_data)

        # Interazioni con tabella
        self.vista.table_programmazione.setEditTriggers(QTableWidget.NoEditTriggers)
        self.vista.table_programmazione.doubleClicked.connect(self.assegna_data)

    def get_data(self):
        data = self.vista.calendar.selectedDate()
        self.vista.label_data.setText(data.toString('dddd, d MMMM yyyy'))

    def assegna_data(self, item):
        self.vista.table_programmazione.setItem(item.row(), item.column(), QTableWidgetItem(str(self.vista.filmName.text())))

    def save(self):
        # aggiungere istruzioni per salvare film e poi chiude il widget
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)

    def go_back(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)
        self.widget.removeWidget(self.vista)
