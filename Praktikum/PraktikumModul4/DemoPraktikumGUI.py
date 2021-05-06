import sys
from PraktikumGUI import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class DemoPraktikumGUI(QDialog):
    def __init__(self,parent = None):
        QDialog. __init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.halo.clicked.connect(self.haloClicked)

    def haloClicked(self):
        QMessageBox.information(self, 'Demo Qt Designer','Hallo %s, apa kabar?' % self.ui.namaEdit.text())

if __name__ == "__main__":
    a = QApplication(sys.argv)
    form = DemoPraktikumGUI()
    form.show()
    a.exec_()