# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(672, 319)
        self.checkBoxCheese = QtWidgets.QCheckBox(Dialog)
        self.checkBoxCheese.setGeometry(QtCore.QRect(310, 50, 191, 22))
        self.checkBoxCheese.setObjectName("checkBoxCheese")
        self.checkBoxOlives = QtWidgets.QCheckBox(Dialog)
        self.checkBoxOlives.setGeometry(QtCore.QRect(310, 100, 151, 22))
        self.checkBoxOlives.setObjectName("checkBoxOlives")
        self.checkBoxSausages = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSausages.setGeometry(QtCore.QRect(310, 150, 181, 22))
        self.checkBoxSausages.setObjectName("checkBoxSausages")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 20, 201, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 191, 17))
        self.label_2.setObjectName("label_2")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(60, 210, 491, 51))
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.checkBoxCheese.setText(_translate("Dialog", "Extra Cheese $1"))
        self.checkBoxOlives.setText(_translate("Dialog", "Extra Olives $1"))
        self.checkBoxSausages.setText(_translate("Dialog", "Extra Sausages $2"))
        self.label.setText(_translate("Dialog", "Regular Pizza $10"))
        self.label_2.setText(_translate("Dialog", "Select your extra toppings"))
