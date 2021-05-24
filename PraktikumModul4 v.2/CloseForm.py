from PyQt5.QtWidgets import QWidget, QPushButton

# from OtherForm import *

class CloseForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(300, 200)
        self.move(300, 300)
        self.setWindowTitle('Demo Menutup Form')
        self.button = QPushButton('Exit')
        self.button.move(50,50)
        self.button.setParent(self)
        self.button.clicked.connect(self.buttonClick)

    def buttonClick(self):
        form = OtherForm()
        form.show()

import sys
from PyQt5.QtWidgets import QApplication
from CloseForm import *
if __name__ == '__main__':
    a = QApplication(sys.argv)
    minform = CloseForm()
    minform.show()
    a.exec_()