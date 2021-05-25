import sys
from PyQt5.QtWidgets import QApplication, QWidget

from home.view.VistaHome import Ui_HOME

if __name__ == '__main__':
    app = QApplication(sys.argv)
    HOME = QWidget()
    vista_home = Ui_HOME()
    vista_home.setupUi(HOME)
    HOME.show()
    sys.exit(app.exec())
