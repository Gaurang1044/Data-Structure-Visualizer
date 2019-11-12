from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType

ui, _ = loadUiType('panga.ui')

# global ww, i, s, x, y, p
# i = 0
# x, y, p = 490, 360, 30
# ww = [1, 2, 3]


class MainApp(QMainWindow, ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ww = []
        self.i = -1
        self.x, self.y, self.p = 490, 440, 21
        self.s = "gLineEdit"
        self.sz = 21

        self.handle_buttons()

    def handle_buttons(self):
        self.pushButton.clicked.connect(self.push)
        self.popButton.clicked.connect(self.pop)
        self.topButton.clicked.connect(self.top)
        self.sizeButton.clicked.connect(self.size)

    def size(self):
        # self.sz = int(self.sizeEdit.text())
        # self.popEdit.setText("9")
        self.pushButton.setEnabled(True)
        self.popButton.setEnabled(True)
        self.topButton.setEnabled(True)
        self.sizeButton.setEnabled(False)

    def push(self):
        self.topEdit.setText("")
        self.label.setText("")
        self.popEdit.setText("")
        data = self.pushEdit.text().strip()

        if self.i == self.sz:
            self.label.setText("Stack is Full")
        elif data == "":
            self.label.setText("Please Enter a Valid Entry")
        else:
            self.i += 1
            # self.lineEdit_2.setText(str(ww.pop()))

            line_editt = QtWidgets.QLineEdit(self.centralwidget)
            line_editt.setGeometry(QtCore.QRect(self.x, self.y, 113, 20))
            line_editt.setAlignment(QtCore.Qt.AlignCenter)
            line_editt.setReadOnly(True)
            line_editt.setText(data)
            line_editt.setObjectName(self.s + str(self.i))
            line_editt.show()
            self.ww.append(line_editt)
            self.y = self.y - self.p

    def pop(self):
        self.topEdit.setText("")
        self.pushEdit.setText("")
        self.label.setText("")

        if self.i == -1:
            self.label.setText("Stack is Empty")
        else:
            z = self.ww.pop()
            self.popEdit.setText(z.text())
            z.hide()
            z.deleteLater()
            self.i -= 1
            self.y += self.p

    def top(self):
        self.pushEdit.setText("")
        self.popEdit.setText("")
        self.label.setText("")

        if self.i == -1:
            self.label.setText("Stack is Empty")
        else:
            self.topEdit.setText(self.ww[self.i].text())


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
