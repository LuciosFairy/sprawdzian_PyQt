import sys

from PyQt6.QtWidgets import QApplication, QDialog

from layout import Ui_Dialog

from PyQt6 import QtCore, QtGui, QtWidgets

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())