import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget
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
    widget= QStackedWidget()
    Vista_login=ViewLogin()
    Vista_login.show()
    sys.exit(app.exec())

    '''app= QApplication(sys.argv)
    vista_Dipendete = ViewDipendente()
    Vista_Dipendente.show()
    sys.exit(app.exec())
    '''