# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlayerChooseCardUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.newCard = QtWidgets.QPushButton(Dialog)
        self.newCard.setGeometry(QtCore.QRect(280, 270, 111, 23))
        self.newCard.setObjectName("newCard")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.newCard.setText(_translate("Dialog", "新建人物卡……"))
