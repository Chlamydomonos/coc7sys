from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from UI import Main_UI, PlayerChooseCard_UI


class MainUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_ui = Main_UI.Ui_Form()
        self.main_ui.setupUi(self)


class PlayerChooseCardUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.player_choose_card_ui = PlayerChooseCard_UI.Ui_Dialog()
        self.player_choose_card_ui.setupUi(self)