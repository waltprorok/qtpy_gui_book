#!/usr/bin/env/python3

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Chapter1.demoLineEdit import *


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ButtonClickMe.clicked.connect(self.display_message)
        self.show()

    def display_message(self):
        self.ui.labelResponse.setText("Hello " + self.ui.lineEditName.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
