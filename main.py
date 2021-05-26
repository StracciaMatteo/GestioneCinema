import sys
from PyQt5.QtWidgets import QApplication, QWidget
from Login.View.ViewLogin import ViewLogin
from home.view.VistaHome import VistaHome

if __name__ == '__main__':
    '''app = QApplication(sys.argv)
    HOME = QWidget()
    vista_home = VistaHome()
    vista_home.setupUi(HOME)
    HOME.show()
    sys.exit(app.exec())'''

    app=QApplication(sys.argv)
    Vista_login=ViewLogin()
    Vista_login.show()
    sys.exit(app.exec())