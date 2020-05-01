# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.player_mode = QtWidgets.QPushButton(Form)
        self.player_mode.setGeometry(QtCore.QRect(90, 210, 75, 23))
        self.player_mode.setObjectName("player_mode")
        self.keeper_mode = QtWidgets.QPushButton(Form)
        self.keeper_mode.setGeometry(QtCore.QRect(240, 210, 75, 23))
        self.keeper_mode.setObjectName("keeper_mode")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.player_mode.setText(_translate("Form", "玩家"))
        self.keeper_mode.setText(_translate("Form", "KP"))
