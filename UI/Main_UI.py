# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 231)
        self.player_mode = QtWidgets.QPushButton(Form)
        self.player_mode.setGeometry(QtCore.QRect(60, 140, 75, 41))
        font = QtGui.QFont()
        font.setFamily("方正毡笔黑简体")
        font.setPointSize(18)
        self.player_mode.setFont(font)
        self.player_mode.setObjectName("player_mode")
        self.keeper_mode = QtWidgets.QPushButton(Form)
        self.keeper_mode.setGeometry(QtCore.QRect(230, 140, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Kozuka Gothic Pr6N H")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.keeper_mode.setFont(font)
        self.keeper_mode.setObjectName("keeper_mode")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 351, 21))
        font = QtGui.QFont()
        font.setFamily("方正北魏楷书简体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 80, 151, 21))
        font = QtGui.QFont()
        font.setFamily("方正北魏楷书简体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 200, 161, 21))
        font = QtGui.QFont()
        font.setFamily("方正北魏楷书简体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.player_mode.setText(_translate("Form", "玩家"))
        self.keeper_mode.setText(_translate("Form", "KP"))
        self.label.setText(_translate("Form", "欢迎来到COC7远程游戏系统测试版V0.1"))
        self.label_2.setText(_translate("Form", "请选择你的身份："))
        self.label_3.setText(_translate("Form", "By Chlamydomonos"))
