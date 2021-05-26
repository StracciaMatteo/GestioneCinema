import sys
from PyQt5.QtWidgets import QApplication, QWidget
from Login.View.ViewLogin import ViewLogin
from home.view.VistaHome import Ui_HOME

if __name__ == '__main__':
    '''app = QApplication(sys.argv)
    HOME = QWidget()
    vista_home = Ui_HOME()
    vista_home.setupUi(HOME)
    HOME.show()
    sys.exit(app.exec())'''

    app=QApplication(sys.argv)
    Vista_login=ViewLogin()
    Vista_login.show()
    sys.exit(app.exec())