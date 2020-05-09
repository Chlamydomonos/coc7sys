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
        Form.resize(300, 161)
        self.professions = QtWidgets.QComboBox(Form)
        self.professions.setGeometry(QtCore.QRect(120, 19, 131, 22))
        self.professions.setObjectName("professions")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 101, 21))
        self.label_3.setObjectName("label_3")
        self.next_step = QtWidgets.QPushButton(Form)
        self.next_step.setGeometry(QtCore.QRect(210, 130, 75, 23))
        self.next_step.setObjectName("next_step")
        self.professional_skills = QtWidgets.QTextBrowser(Form)
        self.professional_skills.setGeometry(QtCore.QRect(20, 70, 256, 41))
        self.professional_skills.setObjectName("professional_skills")
        self.skill_points = QtWidgets.QLabel(Form)
        self.skill_points.setGeometry(QtCore.QRect(100, 131, 54, 21))
        self.skill_points.setObjectName("skill_points")

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
