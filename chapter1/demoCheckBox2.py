# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckBox2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(621, 425)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 10, 66, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBoxIceCreams = QtWidgets.QGroupBox(Dialog)
        self.groupBoxIceCreams.setGeometry(QtCore.QRect(250, 40, 301, 131))
        self.groupBoxIceCreams.setObjectName("groupBoxIceCreams")
        self.checkBoxChocolateChips = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxChocolateChips.setGeometry(QtCore.QRect(0, 30, 201, 22))
        self.checkBoxChocolateChips.setObjectName("checkBoxChocolateChips")
        self.checkBoxCookieDough = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxCookieDough.setGeometry(QtCore.QRect(0, 50, 181, 22))
        self.checkBoxCookieDough.setObjectName("checkBoxCookieDough")
        self.checkBoxRockyRoad = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxRockyRoad.setGeometry(QtCore.QRect(0, 90, 171, 22))
        self.checkBoxRockyRoad.setObjectName("checkBoxRockyRoad")
        self.checkBoxChocolateAlmond = QtWidgets.QCheckBox(self.groupBoxIceCreams)
        self.checkBoxChocolateAlmond.setGeometry(QtCore.QRect(0, 70, 171, 22))
        self.checkBoxChocolateAlmond.setObjectName("checkBoxChocolateAlmond")
        self.groupBoxDrinks = QtWidgets.QGroupBox(Dialog)
        self.groupBoxDrinks.setGeometry(QtCore.QRect(250, 200, 270, 100))
        self.groupBoxDrinks.setObjectName("groupBoxDrinks")
        self.checkBoxCoffee = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxCoffee.setGeometry(QtCore.QRect(0, 30, 96, 22))
        self.checkBoxCoffee.setObjectName("checkBoxCoffee")
        self.checkBoxSoda = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxSoda.setGeometry(QtCore.QRect(0, 50, 96, 22))
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.checkBoxTea = QtWidgets.QCheckBox(self.groupBoxDrinks)
        self.checkBoxTea.setGeometry(QtCore.QRect(0, 70, 96, 22))
        self.checkBoxTea.setObjectName("checkBoxTea")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 150, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 210, 150, 18))
        self.label_3.setObjectName("label_3")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(40, 340, 611, 71))
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Menu"))
        self.groupBoxIceCreams.setTitle(_translate("Dialog", "IceCreams"))
        self.checkBoxChocolateChips.setText(_translate("Dialog", "Mint Chocolate Chips $4"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough $2"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road $5"))
        self.checkBoxChocolateAlmond.setText(_translate("Dialog", "Chocolate Almond $3"))
        self.groupBoxDrinks.setTitle(_translate("Dialog", "Drinks"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee $2"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda $3"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea $1"))
        self.label_2.setText(_translate("Dialog", "Select your IceCream"))
        self.label_3.setText(_translate("Dialog", "Select your drink"))

