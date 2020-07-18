from PyQt5.QtWidgets import QWidget, QSpinBox
from UI import Main_UI, PlayerChooseCard_UI, CreateCardInfo_UI, AdjustBasics_UI, \
    ChooseProfession_UI, ChooseProfessionalSkills_UI, AddSkillPoints_UI
from GameSystem import CreateCard, Profession, Dice, SkillList


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

    def complete(self):
        return self.info_complete


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
            tempui.CON.setEnabled(False)
            tempui.DEX.setEnabled(False)
            self.temp1 = 5
            self.basics[7] -= 5
        elif age < 40:
            tempui.tip.setText('对教育进行 1 次增强检定。')
            tempui.STR.setEnabled(False)
            tempui.CON.setEnabled(False)
            tempui.SIZ.setEnabled(False)
            tempui.DEX.setEnabled(False)
            self.ImproveEDU(1)
            self.basics_complete = True
        elif age < 50:
            tempui.tip.setText('对教育进行 2 次增强检定。力量体质敏\n捷合计减 5 点。外貌减 5 点。')
            tempui.SIZ.setEnabled(False)
            self.temp2 = 5
            self.basics[4] -= 5
            self.ImproveEDU(2)
        elif age < 60:
            tempui.tip.setText('对教育进行 3 次增强检定。力量体质敏\n捷合计减 10 点。外貌减 10 点。')
            tempui.SIZ.setEnabled(False)
            self.temp2 = 10
            self.basics[4] -= 10
            self.ImproveEDU(3)
        elif age < 70:
            tempui.tip.setText('对教育进行 4 次增强检定。力量体质\n敏捷合计减 20 点。外貌减 15 点。')
            tempui.SIZ.setEnabled(False)
            self.temp2 = 20
            self.basics[4] -= 15
            self.ImproveEDU(4)
        elif age < 80:
            tempui.tip.setText('对教育进行 4 次增强检定。力量体\n质敏捷合计减 40 点。外貌减 20 点。')
            tempui.SIZ.setEnabled(False)
            self.temp2 = 40
            self.basics[4] -= 20
            self.ImproveEDU(4)
        else:
            tempui.tip.setText('对教育进行 4 次增强检定。力量体\n质敏捷合计减 80 点。外貌减 25 点。')
            tempui.SIZ.setEnabled(False)
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
        elif self.temp2 != 0:
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

    def complete(self):
        return self.basics_complete


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

    def get_info_from_last_ui(self, last_ui):
        self.basics = last_ui.basics
        self.info = last_ui.info

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
            tempui.min_credit.setText(str(self.profession.get_min_credit()))
            tempui.max_credit.setText(str(self.profession.get_max_credit()))
            self.profession_complete = True
        else:
            tempui.professional_skills.setText('')
            tempui.skill_points.setText('###')
            tempui.min_credit.setText('###')
            tempui.max_credit.setText('###')
            tempui.skill_points_introduction.setText('未定义')
            self.profession_complete = False
            tempui.introduction.setText('')

    def complete(self):
        return self.profession_complete


class ChooseProfessionalSkillsUI(QWidget):
    def __init__(self):
        self.choose_professional_skills_ui = ChooseProfessionalSkills_UI.Ui_Form()
        QWidget.__init__(self)
        self.choose_professional_skills_ui.setupUi(self)
        self.info = []
        self.basics = []
        self.profession = Profession.Profession('', 0, [], 0, [], [])
        self.professional_skills = []
        self.is_professional_skill = []
        self.sub_skills = []
        self.check_boxes = []
        self.combo_boxes = []
        self.initialize_skills()
        self.initialize_sub_skills()
        self.choose_professional_skills_ui.next_step.clicked.connect(self.check_professional_skills)
        self.skills_complete = False

    def initialize_skills(self):
        tempui = self.choose_professional_skills_ui
        self.check_boxes = [tempui.skill1, tempui.skill2, tempui.skill3, tempui.skill4, tempui.skill5,
                            tempui.skill6, tempui.skill7, tempui.skill8, tempui.skill9, tempui.skill10,
                            tempui.skill11, tempui.skill12, tempui.skill13, tempui.skill14, tempui.skill15,
                            tempui.skill16, tempui.skill17, tempui.skill18, tempui.skill19, tempui.skill20,
                            tempui.skill21, tempui.skill22, tempui.skill23, tempui.skill24, tempui.skill25,
                            tempui.skill26, tempui.skill27, tempui.skill28, tempui.skill29, tempui.skill30,
                            tempui.skill31, tempui.skill32, tempui.skill33, tempui.skill34, tempui.skill35,
                            tempui.skill36, tempui.skill37, tempui.skill38, tempui.skill39, tempui.skill40,
                            tempui.skill41, tempui.skill42, tempui.skill43, tempui.skill44, tempui.skill45,
                            tempui.skill46, tempui.skill47, tempui.skill48, tempui.skill49, tempui.skill50,
                            tempui.skill51, tempui.skill52, tempui.skill53, tempui.skill54, tempui.skill55,
                            tempui.skill56, tempui.skill57, tempui.skill58, tempui.skill50, tempui.skill60]

    def initialize_sub_skills(self):
        tempui = self.choose_professional_skills_ui
        self.combo_boxes = [tempui.sub_skill5, tempui.sub_skill6, tempui.sub_skill7,
                            tempui.sub_skill20, tempui.sub_skill21,
                            tempui.sub_skill23, tempui.sub_skill24,
                            tempui.sub_skill29, tempui.sub_skill30, tempui.sub_skill31, tempui.sub_skill32,
                            tempui.sub_skill44,
                            tempui.sub_skill48, tempui.sub_skill49, tempui.sub_skill50,
                            tempui.sub_skill54, tempui.sub_skill55,
                            tempui.sub_skill59, tempui.sub_skill60]
        for i in self.combo_boxes:
            i.addItem('无')
        tempui.sub_skill5.addItems(list(SkillList.art_initial_skills.keys()))
        tempui.sub_skill6.addItems(list(SkillList.art_initial_skills.keys()))
        tempui.sub_skill7.addItems(list(SkillList.art_initial_skills.keys()))
        tempui.sub_skill20.addItems(list(SkillList.fighting_initial_skills.keys()))
        tempui.sub_skill21.addItems(list(SkillList.fighting_initial_skills.keys()))
        tempui.sub_skill23.addItems(list(SkillList.firearms_initial_skills.keys()))
        tempui.sub_skill24.addItems(list(SkillList.firearms_initial_skills.keys()))
        tempui.sub_skill29.addItems(list(SkillList.language_initial_skills.keys()))
        tempui.sub_skill30.addItems(list(SkillList.language_initial_skills.keys()))
        tempui.sub_skill31.addItems(list(SkillList.language_initial_skills.keys()))
        tempui.sub_skill32.addItems(list(SkillList.mother_language_initial_skill.keys()))
        tempui.sub_skill44.addItems(list(SkillList.pilot_initial_skills.keys()))
        tempui.sub_skill48.addItems(list(SkillList.science_initial_skills.keys()))
        tempui.sub_skill49.addItems(list(SkillList.science_initial_skills.keys()))
        tempui.sub_skill50.addItems(list(SkillList.science_initial_skills.keys()))
        tempui.sub_skill54.addItems(list(SkillList.survival_initial_skills.keys()))
        tempui.sub_skill55.addItems(list(SkillList.survival_initial_skills.keys()))
        tempui.sub_skill59.addItems(list(SkillList.special_initial_skills.keys()))
        tempui.sub_skill60.addItems(list(SkillList.knowledge_initial_skills.keys()))

    def get_info_from_last_ui(self, last_UI):
        self.info = last_UI.info
        self.basics = last_UI.basics
        self.profession = last_UI.profession
        self.choose_professional_skills_ui.professional_skills.setText(self.profession.get_skills_introduction())

    def check_professional_skills(self):
        templist = list(SkillList.initial_skills_dict.keys())
        tempui = self.choose_professional_skills_ui
        self.professional_skills = []
        self.is_professional_skill = []
        self.sub_skills = []
        self.skills_complete = False
        for i in range(len(self.check_boxes)):
            self.is_professional_skill.append(self.check_boxes[i].isChecked())
            if self.check_boxes[i].isChecked():
                self.professional_skills.append(templist[i])

        temp1 = len(self.profession.professional_skills_r3)
        temp2 = 0
        for i in self.profession.professional_skills_r2:
            temp2 += i.amount
        temp3 = self.profession.professional_skills_r1 + temp1 + temp2

        for i in self.profession.professional_skills_r3:
            if isinstance(i, list):
                for k in self.combo_boxes:
                    if (k.currentText() == i[1]) & (self.check_boxes[int(k.property('skill')) - 1].isChecked()):
                        temp1 -= 1
            else:
                for j in self.professional_skills:
                    if i == j:
                        temp1 -= 1

        if temp1 == 0:
            for i in self.profession.professional_skills_r2:
                if i.check(self.professional_skills):
                    temp2 -= i.amount
        if temp2 == 0:
            if len(self.professional_skills) == temp3:
                self.skills_complete = True

        for i in self.combo_boxes:
            if (i.currentText() == '无') & (self.check_boxes[i.property('skill') - 1].isChecked()):
                self.skills_complete = False
            for j in self.combo_boxes:
                if (i.currentText() == j.currentText()) & (i.currentText() != '无') & (i.property('skill') !=
                                                                                      j.property('skill')):
                    self.skills_complete = False

        if tempui.sub_skill32.currentText() == '无':
            self.skills_complete = False

        for i in self.combo_boxes:
            self.sub_skills.append(i.currentText())

    def complete(self):
        return self.skills_complete


class AddSkillPointsUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.add_skill_points_ui = AddSkillPoints_UI.Ui_Form()
        self.add_skill_points_ui.setupUi(self)
        self.info = []
        self.basics = []
        self.profession = Profession.Profession('', 0, [], 0, [], [])
        self.professional_skills = []
        self.is_professional_skill = []
        self.sub_skills = []
        self.professional_skill_points = []
        self.interest_skill_points = []
        self.professional_spin_boxes = []
        self.interest_spin_boxes = []
        self.sub_spin_boxes = []
        self.sub_skill_labels = []
        self.checked_professional_skills = []
        self.initials = []
        self.sum_labels = []
        self.professional_points_left = 0
        self.interest_points_left = 0
        self.points_complete = False

    class CheckedSkill:
        def __init__(self, professional: QSpinBox, interest: QSpinBox):
            self.professional = professional
            self.interest = interest
            self.ispr = False
            self.max_point = 0
            self.initial = 0

        def get_pr(self):
            return self.professional.value()

        def get_in(self):
            return self.interest.value()

        def set_max_pr(self, max_pr):
            self.professional.setMaximum(max_pr)

        def set_max_in(self, max_in):
            self.interest.setMaximum(max_in)

        def set_is_professional(self, ispr):
            self.ispr = ispr

        def set_initial(self, initial):
            self.initial = initial
            if self.ispr:
                self.max_point = 90 - self.initial
            else:
                self.max_point = 70 - self.initial

        def get_sum_point(self):
            return self.initial + self.professional.value() + self.interest.value()

        def calculate_max_point(self, left_pr, left_in):
            current_pr = self.professional.value()
            current_in = self.interest.value()
            max_pr = min(self.max_point - current_in, current_pr + left_pr)
            max_in = min(self.max_point - current_pr, current_in + left_in)
            self.professional.setMaximum(max_pr)
            self.interest.setMaximum(max_in)

    def get_info_from_last_ui(self, last_ui):
        self.info = last_ui.info
        self.basics = last_ui.basics
        self.profession = last_ui.profession
        self.professional_skills = last_ui.professional_skills
        self.is_professional_skill = last_ui.is_professional_skill
        self.sub_skills = last_ui.sub_skills
        self.initialize_labels()
        self.initialize_spin_boxes()
        self.initialize_initials()
        self.initialize_checked_skills()
        self.check_skill_points()

    def initialize_initials(self):
        temp = 0
        for i in range(len(SkillList.initial_skills_list)):
            if isinstance(SkillList.initial_skills_list[i], dict):
                self.initials.append(SkillList.initial_skills_list[i][self.sub_skills[temp]].initial)
            else:
                self.initials.append(SkillList.initial_skills_list[i].initial)

    def initialize_spin_boxes(self):
        tempui = self.add_skill_points_ui
        self.professional_spin_boxes = [
            tempui.pr1, tempui.pr2, tempui.pr3, tempui.pr4, tempui.pr5, tempui.pr6,
            tempui.pr7, tempui.pr8, tempui.pr9, tempui.pr10, tempui.pr11, tempui.pr12,
            tempui.pr13, tempui.pr14, tempui.pr15, tempui.pr16, tempui.pr17, tempui.pr18,
            tempui.pr19, tempui.pr20, tempui.pr21, tempui.pr22, tempui.pr23, tempui.pr24,
            tempui.pr25, tempui.pr26, tempui.pr27, tempui.pr28, tempui.pr29, tempui.pr30,
            tempui.pr31, tempui.pr32, tempui.pr33, tempui.pr34, tempui.pr35, tempui.pr36,
            tempui.pr37, tempui.pr38, tempui.pr39, tempui.pr40, tempui.pr41, tempui.pr42,
            tempui.pr43, tempui.pr44, tempui.pr45, tempui.pr46, tempui.pr47, tempui.pr48,
            tempui.pr49, tempui.pr50, tempui.pr51, tempui.pr52, tempui.pr53, tempui.pr54,
            tempui.pr55, tempui.pr56, tempui.pr57, tempui.pr58, tempui.pr59, tempui.pr60
        ]
        self.interest_spin_boxes= [
            tempui.in1, tempui.in2, tempui.in3, tempui.in4, tempui.in5, tempui.in6,
            tempui.in7, tempui.in8, tempui.in9, tempui.in10, tempui.in11, tempui.in12,
            tempui.in13, tempui.in14, tempui.in15, tempui.in16, tempui.in17, tempui.in18,
            tempui.in19, tempui.in20, tempui.in21, tempui.in22, tempui.in23, tempui.in24,
            tempui.in25, tempui.in26, tempui.in27, tempui.in28, tempui.in29, tempui.in30,
            tempui.in31, tempui.in32, tempui.in33, tempui.in34, tempui.in35, tempui.in36,
            tempui.in37, tempui.in38, tempui.in39, tempui.in40, tempui.in41, tempui.in42,
            tempui.in43, tempui.in44, tempui.in45, tempui.in46, tempui.in47, tempui.in48,
            tempui.in49, tempui.in50, tempui.in51, tempui.in52, tempui.in53, tempui.in54,
            tempui.in55, tempui.in56, tempui.in57, tempui.in58, tempui.in59, tempui.in60
        ]

        self.sub_spin_boxes = [
            tempui.in5, tempui.in6, tempui.in7,
            tempui.in20, tempui.in21, tempui.in23, tempui.in24,
            tempui.in29, tempui.in30, tempui.in31, tempui.in32,
            tempui.in44, tempui.in48, tempui.in49, tempui.in50,
            tempui.in54, tempui.in55, tempui.in59, tempui.in60
        ]

        for i in range(len(self.is_professional_skill)):
            if not self.is_professional_skill[i]:
                self.professional_spin_boxes[i].setEnabled(False)

        tempui.pr11.setEnabled(True)

        for i in range(len(self.sub_skills)):
            if self.sub_skills[i] == '无':
                self.sub_spin_boxes[i].setEnabled(False)

        tempui.pr11.setMinimum(self.profession.credit[0])
        tempui.pr11.setValue(self.profession.credit[0])

        for i in self.professional_spin_boxes + self.interest_spin_boxes:
            i.setMaximum(90)
            i.valueChanged.connect(self.check_skill_points)

    def initialize_labels(self):
        tempui = self.add_skill_points_ui
        self.sub_skill_labels = [
            tempui.sub_skill5, tempui.sub_skill6, tempui.sub_skill7,
            tempui.sub_skill20, tempui.sub_skill21, tempui.sub_skill23, tempui.sub_skill24,
            tempui.sub_skill29, tempui.sub_skill30, tempui.sub_skill31, tempui.sub_skill32,
            tempui.sub_skill44, tempui.sub_skill48, tempui.sub_skill49, tempui.sub_skill50,
            tempui.sub_skill54, tempui.sub_skill55, tempui.sub_skill59, tempui.sub_skill60
        ]

        self.sum_labels = [
            tempui.sum_1, tempui.sum_2, tempui.sum_3, tempui.sum_4, tempui.sum_5, tempui.sum_6,
            tempui.sum_7, tempui.sum_8, tempui.sum_9, tempui.sum_10, tempui.sum_11, tempui.sum_12,
            tempui.sum_13, tempui.sum_14, tempui.sum_15, tempui.sum_16, tempui.sum_17, tempui.sum_18,
            tempui.sum_19, tempui.sum_20, tempui.sum_21, tempui.sum_22, tempui.sum_23, tempui.sum_24,
            tempui.sum_25, tempui.sum_26, tempui.sum_27, tempui.sum_28, tempui.sum_29, tempui.sum_30,
            tempui.sum_31, tempui.sum_32, tempui.sum_33, tempui.sum_34, tempui.sum_35, tempui.sum_36,
            tempui.sum_37, tempui.sum_38, tempui.sum_39, tempui.sum_40, tempui.sum_41, tempui.sum_42,
            tempui.sum_43, tempui.sum_44, tempui.sum_45, tempui.sum_46, tempui.sum_47, tempui.sum_48,
            tempui.sum_49, tempui.sum_50, tempui.sum_51, tempui.sum_52, tempui.sum_53, tempui.sum_54,
            tempui.sum_55, tempui.sum_56, tempui.sum_57, tempui.sum_58, tempui.sum_59, tempui.sum_60
        ]

        for i in range(len(self.sub_skills)):
            self.sub_skill_labels[i].setText(self.sub_skills[i])

        self.professional_points_left = self.profession.skill_points.calculate(self.basics)
        tempui.professional_points.setText(str(self.professional_points_left))
        self.interest_points_left = self.basics[5] * 2
        tempui.interest_points.setText(str(self.interest_points_left))
        tempui.min_credit.setText(str(self.profession.credit[0]))
        tempui.max_credit.setText(str(self.profession.credit[1]))

    def initialize_checked_skills(self):
        for i in range(len(self.is_professional_skill)):
            temp_skill = self.CheckedSkill(self.professional_spin_boxes[i], self.interest_spin_boxes[i])
            temp_skill.set_is_professional(self.is_professional_skill[i])
            temp_skill.set_initial(self.initials[i])
            self.checked_professional_skills.append(temp_skill)

    def check_skill_points(self):
        tempui = self.add_skill_points_ui
        self.professional_points_left = self.profession.skill_points.calculate(self.basics)
        self.interest_points_left = self.basics[5] * 2
        for i in self.checked_professional_skills:
            self.professional_points_left -= i.get_pr()
            self.interest_points_left -= i.get_in()
        tempui.professional_points.setText(str(self.professional_points_left))
        tempui.interest_points.setText(str(self.interest_points_left))

        for i in self.checked_professional_skills:
            i.calculate_max_point(self.professional_points_left, self.interest_points_left)

        for i in range(len(self.checked_professional_skills)):
            self.sum_labels[i].setText(str(self.checked_professional_skills[i].get_sum_point()))

        tempui.pr11.setMaximum(min(self.profession.credit[1], tempui.pr11.value() + self.professional_points_left))

        if self.professional_points_left == 0 and self.interest_points_left == 0:
            self.points_complete = True

    def complete(self):
        return self.points_complete
