# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlayerChooseCard_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.new_card = QtWidgets.QPushButton(Form)
        self.new_card.setGeometry(QtCore.QRect(280, 270, 111, 23))
        self.new_card.setObjectName("new_card")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.new_card.setText(_translate("Form", "新建人物卡……"))
