# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChooseProfession_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(391, 329)
        self.professions = QtWidgets.QComboBox(Form)
        self.professions.setGeometry(QtCore.QRect(120, 19, 241, 22))
        self.professions.setObjectName("professions")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 108, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 168, 101, 21))
        self.label_3.setObjectName("label_3")
        self.next_step = QtWidgets.QPushButton(Form)
        self.next_step.setGeometry(QtCore.QRect(300, 298, 75, 23))
        self.next_step.setObjectName("next_step")
        self.professional_skills = QtWidgets.QTextBrowser(Form)
        self.professional_skills.setGeometry(QtCore.QRect(20, 128, 361, 41))
        self.professional_skills.setObjectName("professional_skills")
        self.skill_points = QtWidgets.QLabel(Form)
        self.skill_points.setGeometry(QtCore.QRect(80, 189, 21, 21))
        self.skill_points.setObjectName("skill_points")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 208, 101, 21))
        self.label_4.setObjectName("label_4")
        self.introduction = QtWidgets.QTextBrowser(Form)
        self.introduction.setGeometry(QtCore.QRect(10, 228, 371, 61))
        self.introduction.setObjectName("introduction")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 190, 21, 20))
        self.label_5.setObjectName("label_5")
        self.skill_points_introduction = QtWidgets.QLabel(Form)
        self.skill_points_introduction.setGeometry(QtCore.QRect(130, 190, 251, 20))
        self.skill_points_introduction.setObjectName("skill_points_introduction")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 50, 101, 21))
        self.label_6.setObjectName("label_6")
        self.min_credit = QtWidgets.QLabel(Form)
        self.min_credit.setGeometry(QtCore.QRect(80, 80, 21, 21))
        self.min_credit.setObjectName("min_credit")
        self.skill_points_3 = QtWidgets.QLabel(Form)
        self.skill_points_3.setGeometry(QtCore.QRect(110, 80, 16, 21))
        self.skill_points_3.setObjectName("skill_points_3")
        self.max_credit = QtWidgets.QLabel(Form)
        self.max_credit.setGeometry(QtCore.QRect(130, 80, 21, 21))
        self.max_credit.setObjectName("max_credit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "请选择职业："))
        self.label_2.setText(_translate("Form", "该职业的本职技能："))
        self.label_3.setText(_translate("Form", "该职业的技能点数："))
        self.next_step.setText(_translate("Form", "下一步"))
        self.skill_points.setText(_translate("Form", "###"))
        self.label_4.setText(_translate("Form", "该职业的简介："))
        self.label_5.setText(_translate("Form", "——"))
        self.skill_points_introduction.setText(_translate("Form", "未定义"))
        self.label_6.setText(_translate("Form", "该职业的信用范围："))
        self.min_credit.setText(_translate("Form", "###"))
        self.skill_points_3.setText(_translate("Form", "-"))
        self.max_credit.setText(_translate("Form", "###"))
