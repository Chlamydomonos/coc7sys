from PyQt5.QtWidgets import QWidget
from UI import Main_UI, PlayerChooseCard_UI, CreateCardInfo_UI, AdjustBasics_UI, \
    ChooseProfession_UI
from GameSystem import CreateCard, Profession, Dice


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
        self.info_complete = False
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
        temp_complete = 0
        if (name != '') & (sex != 2) & (age >= 15) & (age <= 90) & (living_place != '') & (homeland != ''):
            temp_complete = 1
        if (age >= 70) & (age < 80):
            if self.basics[4] < 20:
                temp_complete = 0
        if age >= 80:
            if self.basics[4] < 25:
                temp_complete = 0
            elif self.basics[0] + self.basics[1] + self.basics[3] < 80:
                temp_complete = 0
        if temp_complete == 1:
            self.info_complete = True
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
        self.basics_complete = False

    def get_info_from_last_UI(self, last_UI):
        self.basics = last_UI.basics
        self.info = last_UI.info

    def initialize_UI(self):
        tempui = self.adjust_basics_ui

        tempui.old_STR.setText(str(self.basics[0]))
        tempui.old_CON.setText(str(self.basics[1]))
        tempui.old_SIZ.setText(str(self.basics[2]))
        tempui.old_DEX.setText(str(self.basics[3]))
        tempui.old_APP.setText(str(self.basics[4]))
        tempui.old_INT.setText(str(self.basics[5]))
        tempui.old_POW.setText(str(self.basics[6]))
        tempui.old_EDU.setText(str(self.basics[7]))

        age = self.info[2]
        tempui.age.setText(str(age))
        if age < 20:
            tempui.tip.setText('力量和体型合计减 5 点。教育减 5 点。决定\n幸运值时可以骰 2 次并取较好的一次。')
            self.temp1 = 5
            self.basics[7] -= 5
        elif age < 40:
            tempui.tip.setText('对教育进行 1 次增强检定。')
            self.ImproveEDU(1)
            self.basics_complete = True
        elif age < 50:
            tempui.tip.setText('对教育进行 2 次增强检定。力量体质敏\n捷合计减 5 点。外貌减 5 点。')
            self.temp2 = 5
            self.basics[4] -= 5
            self.ImproveEDU(2)
        elif age < 60:
            tempui.tip.setText('对教育进行 3 次增强检定。力量体质敏\n捷合计减 10 点。外貌减 10 点。')
            self.temp2 = 10
            self.basics[4] -= 10
            self.ImproveEDU(3)
        elif age < 70:
            tempui.tip.setText('对教育进行 4 次增强检定。力量体质\n敏捷合计减 20 点。外貌减 15 点。')
            self.temp2 = 20
            self.basics[4] -= 15
            self.ImproveEDU(4)
        elif age < 80:
            tempui.tip.setText('对教育进行 4 次增强检定。力量体\n质敏捷合计减 40 点。外貌减 20 点。')
            self.temp2 = 40
            self.basics[4] -= 20
            self.ImproveEDU(4)
        else:
            tempui.tip.setText('对教育进行 4 次增强检定。力量体\n质敏捷合计减 80 点。外貌减 25 点。')
            self.temp2 = 80
            self.basics[4] -= 25
            self.ImproveEDU(4)
        tempui.STR.setValue(self.basics[0])
        tempui.CON.setValue(self.basics[1])
        tempui.SIZ.setValue(self.basics[2])
        tempui.DEX.setValue(self.basics[3])
        tempui.APP.setValue(self.basics[4])
        tempui.INT.setValue(self.basics[5])
        tempui.POW.setValue(self.basics[6])
        tempui.EDU.setValue(self.basics[7])
        tempui.APP.setRange(self.basics[4], self.basics[4])
        tempui.INT.setRange(self.basics[5], self.basics[5])
        tempui.POW.setRange(self.basics[6], self.basics[6])
        tempui.EDU.setRange(self.basics[7], self.basics[7])
        tempui.STR.setMaximum(self.basics[0])
        tempui.CON.setMaximum(self.basics[1])
        tempui.SIZ.setMaximum(self.basics[2])
        tempui.DEX.setMaximum(self.basics[3])
        self.adjust_basics_ui.STR.valueChanged.connect(self.adjust)
        self.adjust_basics_ui.CON.valueChanged.connect(self.adjust)
        self.adjust_basics_ui.SIZ.valueChanged.connect(self.adjust)
        self.adjust_basics_ui.DEX.valueChanged.connect(self.adjust)
        self.adjust_basics_ui.APP.valueChanged.connect(self.adjust)
        self.adjust_basics_ui.INT.valueChanged.connect(self.adjust)
        self.adjust_basics_ui.POW.valueChanged.connect(self.adjust)
        self.adjust_basics_ui.EDU.valueChanged.connect(self.adjust)

    def ImproveEDU(self, times):
        for i in range(times):
            temp = Dice.D100.throw()
            if temp > self.basics[7]:
                self.basics[7] += Dice.D10.throw()
        if self.basics[7] > 99:
            self.basics[7] = 99

    def adjust(self):
        tempui = self.adjust_basics_ui
        if self.temp1 != 0:
            tempui.CON.setRange(self.basics[1], self.basics[1])
            tempui.DEX.setRange(self.basics[3], self.basics[3])
            changed_values = self.basics[0] - tempui.STR.value() + self.basics[2] - tempui.SIZ.value()
            remaining_values = self.temp1 - changed_values
            tempui.STR.setMinimum(max(tempui.STR.value() - remaining_values, 1))
            tempui.SIZ.setMinimum(max(tempui.SIZ.value() - remaining_values, 1))
            if remaining_values == 0:
                self.basics_complete = True
        elif self. temp2 != 0:
            tempui.SIZ.setRange(self.basics[2], self.basics[2])
            changed_values = self.basics[0] - tempui.STR.value() + self.basics[1] - tempui.CON.value() + \
                             self.basics[3] - tempui.DEX.value()
            remaining_values = self.temp2 - changed_values
            tempui.STR.setMinimum(max(tempui.STR.value() - remaining_values, 1))
            tempui.CON.setMinimum(max(tempui.CON.value() - remaining_values, 1))
            tempui.DEX.setMinimum(max(tempui.DEX.value() - remaining_values, 1))
            if remaining_values == 0:
                self.basics_complete = True
                self.basics = [tempui.STR.value(),
                               tempui.CON.value(),
                               tempui.SIZ.value(),
                               tempui.DEX.value(),
                               tempui.APP.value(),
                               tempui.INT.value(),
                               tempui.POW.value(),
                               tempui.EDU.value()]
        else:
            tempui.STR.setRange(self.basics[0], self.basics[0])
            tempui.CON.setRange(self.basics[1], self.basics[1])
            tempui.SIZ.setRange(self.basics[2], self.basics[2])
            tempui.DEX.setRange(self.basics[3], self.basics[3])
            self.basics_complete = True
        if self.basics_complete:
            self.basics = [tempui.STR.value(),
                           tempui.CON.value(),
                           tempui.SIZ.value(),
                           tempui.DEX.value(),
                           tempui.APP.value(),
                           tempui.INT.value(),
                           tempui.POW.value(),
                           tempui.EDU.value()]


class ChooseProfessionUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.choose_profession_ui = ChooseProfession_UI.Ui_Form()
        self.choose_profession_ui.setupUi(self)
        self.basics = []
        self.info = []
        self.profession = Profession.Profession('', 0, 0, 0, [], [])
        self.initialize_professions()
        self.choose_profession_ui.professions.currentTextChanged.connect(self.get_profession)
        self.profession_complete = False

    def get_info_from_last_UI(self, last_UI):
        self.basics = last_UI.basics
        self.info = last_UI.info

    def initialize_professions(self):
        self.choose_profession_ui.professions.addItem('未选择')
        for i in Profession.professions:
            self.choose_profession_ui.professions.addItem(i)

    def get_profession(self, name):
        tempui = self.choose_profession_ui
        if name != '未选择':
            self.profession = Profession.read_profession(name)
            tempui.professional_skills.setText(self.profession.get_skills_introduction())
            tempui.skill_points.setText(str(self.profession.skill_points.calculate(self.basics)))
            tempui.skill_points_introduction.setText(self.profession.skill_points.get_introduction())
            tempui.introduction.setText(self.profession.read_introduction())
            self.profession_complete = True
        else:
            tempui.professional_skills.setText('')
            tempui.skill_points.setText('###')
            tempui.skill_points_introduction.setText('未定义')
            self.profession_complete = False
            tempui.introduction.setText('')
