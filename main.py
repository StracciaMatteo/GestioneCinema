import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget
from PyQt5 import QtGui

from Login.View.ViewLogin import ViewLogin
from home.view.VistaHome import VistaHome


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = QStackedWidget()

    Vista_login = ViewLogin(widget)
    Vista_home = VistaHome(widget)

    widget.addWidget(Vista_login)
    widget.addWidget(Vista_home)
    widget.setStyleSheet("background-color: rgb(254, 235, 156)")
    widget.setWindowTitle("Cinema")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap("images/biglietto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    widget.setWindowIcon(icon)
    # Spostamento widget al centro (fissare dimensione login al max per mantenere tutto al centro)
    widget.show()
    centerPoint = QtGui.QScreen.availableGeometry(app.primaryScreen()).center()
    fg = widget.frameGeometry()
    fg.moveCenter(centerPoint)
    widget.move(fg.topLeft())

    sys.exit(app.exec())

