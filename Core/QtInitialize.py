import sys
from PyQt5.QtWidgets import QApplication, QWidget
from UI import mainUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    main_ui = mainUI.Ui_Form()
    main_ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
