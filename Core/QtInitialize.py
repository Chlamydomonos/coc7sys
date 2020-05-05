from PyQt5.QtWidgets import QWidget
from UI import Main_UI, PlayerChooseCard_UI, CreateCardInfo_UI
from GameSystem import CreateCard


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
        self.info_complete = 0
        self.info = []
        self.basics = []
        self.random_basics()

    def random_basics(self):
        tempui = self.create_card_info_ui
        basics = CreateCard.random_basics()
        tempui.STR.setText(str(basics[0]))
        tempui.CON.setText(str(basics[1]))
        tempui.SIZ.setText(str(basics[2]))
        tempui.DEX.setText(str(basics[3]))
        tempui.APP.setText(str(basics[4]))
        tempui.INT.setText(str(basics[5]))
        tempui.POW.setText(str(basics[6]))
        tempui.EDU.setText(str(basics[7]))
        self.basics = basics

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
        if (name != '') & (sex != 2) & (age >= 15) & (age <= 90) & (living_place != '') & (homeland != ''):
            self.info_complete = 1
            self.info = [name, sex, age, living_place, homeland]
