from PyQt5.QtWidgets import QWidget
from UI import Main_UI, PlayerChooseCard_UI, CreateCardInfo_UI
from Core import FileIO


class MainUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_ui = Main_UI.Ui_Form()
        self.main_ui.setupUi(self)


class PlayerChooseCardUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.player_choose_card_ui = PlayerChooseCard_UI.Ui_Form()
        self.player_choose_card_ui.setupUi(self)


class CreateCardInfoUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.create_card_info_ui = CreateCardInfo_UI.Ui_Form()
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
        if name != '' & sex != 2 & age >= 15 & age <= 90 & living_place != '' & homeland != '':
            FileIO.save_data('temp0.suondeea', [name, sex, age, living_place, homeland])
