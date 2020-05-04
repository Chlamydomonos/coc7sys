# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateCardInfo_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(224, 193)
        self.sex_0 = QtWidgets.QRadioButton(Form)
        self.sex_0.setGeometry(QtCore.QRect(50, 40, 31, 16))
        self.sex_0.setObjectName("sex_0")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.label.setObjectName("label")
        self.age = QtWidgets.QSpinBox(Form)
        self.age.setGeometry(QtCore.QRect(50, 70, 42, 22))
        self.age.setObjectName("age")
        self.hidden_button_2 = QtWidgets.QPushButton(Form)
        self.hidden_button_2.setGeometry(QtCore.QRect(170, 160, 20, 23))
        self.hidden_button_2.setObjectName("hidden_button_2")
        self.next_step = QtWidgets.QPushButton(Form)
        self.next_step.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.next_step.setObjectName("next_step")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 31, 16))
        self.label_3.setObjectName("label_3")
        self.homeland = QtWidgets.QLineEdit(Form)
        self.homeland.setGeometry(QtCore.QRect(50, 130, 113, 20))
        self.homeland.setObjectName("homeland")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 31, 16))
        self.label_4.setObjectName("label_4")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(50, 10, 113, 20))
        self.name.setObjectName("name")
        self.sex_1 = QtWidgets.QRadioButton(Form)
        self.sex_1.setGeometry(QtCore.QRect(110, 40, 31, 16))
        self.sex_1.setObjectName("sex_1")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 31, 16))
        self.label_5.setObjectName("label_5")
        self.living_place = QtWidgets.QLineEdit(Form)
        self.living_place.setGeometry(QtCore.QRect(50, 100, 113, 20))
        self.living_place.setObjectName("living_place")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sex_0.setText(_translate("Form", "男"))
        self.label.setText(_translate("Form", "姓名："))
        self.hidden_button_2.setText(_translate("Form", "PushButton"))
        self.next_step.setText(_translate("Form", "下一步"))
        self.label_2.setText(_translate("Form", "性别："))
        self.label_3.setText(_translate("Form", "年龄："))
        self.label_4.setText(_translate("Form", "住地："))
        self.sex_1.setText(_translate("Form", "女"))
        self.label_5.setText(_translate("Form", "故乡："))
