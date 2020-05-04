# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateCardInfo_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(239, 189)
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(80, 10, 113, 20))
        self.name.setObjectName("name")
        self.living_place = QtWidgets.QLineEdit(Dialog)
        self.living_place.setGeometry(QtCore.QRect(80, 100, 113, 20))
        self.living_place.setObjectName("living_place")
        self.homeland = QtWidgets.QLineEdit(Dialog)
        self.homeland.setGeometry(QtCore.QRect(80, 130, 113, 20))
        self.homeland.setObjectName("homeland")
        self.age = QtWidgets.QSpinBox(Dialog)
        self.age.setGeometry(QtCore.QRect(80, 70, 42, 22))
        self.age.setObjectName("age")
        self.sex_0 = QtWidgets.QRadioButton(Dialog)
        self.sex_0.setGeometry(QtCore.QRect(80, 40, 31, 16))
        self.sex_0.setObjectName("sex_0")
        self.sex_1 = QtWidgets.QRadioButton(Dialog)
        self.sex_1.setGeometry(QtCore.QRect(140, 40, 31, 16))
        self.sex_1.setObjectName("sex_1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 31, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 70, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 130, 31, 16))
        self.label_5.setObjectName("label_5")
        self.next_step = QtWidgets.QPushButton(Dialog)
        self.next_step.setGeometry(QtCore.QRect(160, 160, 75, 23))
        self.next_step.setObjectName("next_step")
        self.hidden_button = QtWidgets.QPushButton(Dialog)
        self.hidden_button.setGeometry(QtCore.QRect(200, 160, 20, 23))
        self.hidden_button.setObjectName("hidden_button")
        self.name.raise_()
        self.living_place.raise_()
        self.homeland.raise_()
        self.age.raise_()
        self.sex_0.raise_()
        self.sex_1.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.hidden_button.raise_()
        self.next_step.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.sex_0.setText(_translate("Dialog", "男"))
        self.sex_1.setText(_translate("Dialog", "女"))
        self.label.setText(_translate("Dialog", "姓名："))
        self.label_2.setText(_translate("Dialog", "性别："))
        self.label_3.setText(_translate("Dialog", "年龄："))
        self.label_4.setText(_translate("Dialog", "住地："))
        self.label_5.setText(_translate("Dialog", "故乡："))
        self.next_step.setText(_translate("Dialog", "下一步"))
        self.hidden_button.setText(_translate("Dialog", "PushButton"))
