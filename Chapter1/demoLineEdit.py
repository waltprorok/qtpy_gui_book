# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoLineEdit.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 60, 81, 16))
        self.label.setObjectName("label")
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(30, 110, 331, 16))
        self.labelResponse.setText("")
        self.labelResponse.setObjectName("labelResponse")
        self.lineEditName = QtWidgets.QLineEdit(Dialog)
        self.lineEditName.setGeometry(QtCore.QRect(130, 60, 231, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.ButtonClickMe = QtWidgets.QPushButton(Dialog)
        self.ButtonClickMe.setGeometry(QtCore.QRect(130, 210, 91, 23))
        self.ButtonClickMe.setCheckable(False)
        self.ButtonClickMe.setChecked(False)
        self.ButtonClickMe.setObjectName("ButtonClickMe")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter your name"))
        self.ButtonClickMe.setText(_translate("Dialog", "Click"))
