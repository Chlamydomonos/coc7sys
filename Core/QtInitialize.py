from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from UI import Main_UI, PlayerChooseCard_UI, CreateCardInfo_UI


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


class CreateCardInfoUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.create_card_info_ui = CreateCardInfo_UI.Ui_Dialog()
        self.create_card_info_ui.setupUi(self)
        self.create_card_info_ui.next_step.clicked.connect(self.get_info)

    def get_info(self):
        tempui = self.create_card_info_ui
        name = tempui.name.text()
        sex = 2
        if tempui.sex_0.isChecked():
            sex = 0
        if tempui.sex_1.isChecked():
            sex = 1
        age = tempui.age.value()
        living_place = tempui.living_place.text()
        homeland = tempui.homeland.text()
        print('Suon Deea')
