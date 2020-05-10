from PyQt5.QtWidgets import QWidget
from UI import Main_UI, PlayerChooseCard_UI, CreateCardInfo_UI, AdjustBasics_UI,\
    ChooseProfession_UI
from GameSystem import CreateCard, Profession


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


class AdjustBasicsUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.adjust_basics_ui = AdjustBasics_UI.Ui_Form()
        self.adjust_basics_ui.setupUi(self)
        self.basics = []
        self.info = []
        self.temp1 = 0
        self.temp2 = 0

    def get_info_from_last_UI(self, last_UI):
        self.basics = last_UI.basics
        self.info = last_UI.info

    def initialize_UI(self):
        tempui = self.adjust_basics_ui
        tempui.age.setText(str(self.info[2]))
        age = self.info[2]
        if age < 20:
            tempui.tip.setText('力量和体型合计减 5 点。教育减 5 点。决定幸运值时可以骰 2 次并取较好的一次。')
        elif age < 40:
            tempui.tip.setText('对教育进行 1 次增强检定。')
        elif age < 50:
            tempui.tip.setText('对教育进行 2 次增强检定。力量体质敏捷合计减 5 点。外貌减 5 点。')
        elif age < 60:
            tempui.tip.setText('对教育进行 3 次增强检定。力量体质敏捷合计减 10 点。外貌减 10 点。')
        elif age < 70:
            tempui.tip.setText('对教育进行 4 次增强检定。力量体质敏捷合计减 20 点。外貌减 15 点。')
        elif age < 80:
            tempui.tip.setText('对教育进行 4 次增强检定。力量体质敏捷合计减 40 点。外貌减 20 点。')
        else:
            tempui.tip.setText('对教育进行 4 次增强检定。力量体质敏捷合计减 80 点。外貌减 25 点。')

    # def set_adjustment_values(self):


class ChooseProfessionUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.choose_profession_ui = ChooseProfession_UI.Ui_Form()
        self.choose_profession_ui.setupUi(self)
        self.basics = []
        self.info = []
        self.profession = Profession.Profession('', 0, 0, 0, [], [], '')

    def get_info_from_last_UI(self, last_UI):
        self.basics = last_UI.basics
        self.info = last_UI.info

    def initialize_professions(self):
        for i in Profession.professions:
            self.choose_profession_ui.professions.addItem(i.name)