from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType

ui,_ = loadUiType('pproject.ui')

class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.introicon.clicked.connect(self.tabiyat)


def main():
    app= QApplication(sys.argv)
    window= MainApp()
    window.show()
    app.exec_()



if __name__ =='__main__':
    main()