import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5 import QtGui
from Login.View.ViewLogin import ViewLogin
from dipendente.DatiDipendente.view.ViewDipendente import ViewDipendente
from home.view.VistaHome import VistaHome
if __name__ == '__main__':
    '''app = QApplication(sys.argv)
    HOME = QWidget()
    vista_home = VistaHome()
    vista_home.setupUi(HOME)
    HOME.show()
    sys.exit(app.exec())'''

    app=QApplication(sys.argv)

    widget = QStackedWidget()

    Vista_login=ViewLogin(widget)
    Vista_home = VistaHome(widget)

    widget.addWidget(Vista_login)
    widget.addWidget(Vista_home)
    widget.setStyleSheet("background-color: rgb(254, 235, 156)")
    widget.setWindowTitle("Cinema")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("images/biglietto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    widget.setWindowIcon(icon)
    # Vista_login.show()
    # widget.setCurrentWidget(Vista_home)
    widget.show()
    sys.exit(app.exec())

    '''app = QApplication(sys.argv)
    Vista_Dipendente=ViewDipendente()
    Vista_Dipendente.show()
    sys.exit(app.exec())'''
