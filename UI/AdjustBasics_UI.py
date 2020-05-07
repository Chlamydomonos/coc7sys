# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdjustBasics_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(209, 144)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 151, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 201, 21))
        self.label_2.setObjectName("label_2")
        self.next_step = QtWidgets.QPushButton(Form)
        self.next_step.setGeometry(QtCore.QRect(120, 110, 75, 23))
        self.next_step.setObjectName("next_step")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Waiting to be finished..."))
        self.label_2.setText(_translate("Form", "（这本应是依据年龄改变属性的窗口）"))
        self.next_step.setText(_translate("Form", "下一步"))
