import sys
from PyQt5.QtWidgets import QApplication, QWidget
from mainUI import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    ui = Ui_Form()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
