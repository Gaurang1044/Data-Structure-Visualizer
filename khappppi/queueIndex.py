from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType

ui, _ = loadUiType('queue.ui')


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
        self.r = 0
        self.x, self.y, self.p = 490, 440, 21
        self.s = "gLineEdit"
        self.sz = 21

        self.handle_buttons()

    def handle_buttons(self):
        self.pushButton.clicked.connect(self.push)
        self.popButton.clicked.connect(self.pop)
        self.topButton.clicked.connect(self.top)
        self.sizeButton.clicked.connect(self.size)
        self.clearButton.clicked.connect(self.clear)

    def clear(self):
        pass

    def size(self):

        bl = False

        try:
            self.sz = int(self.sizeEdit.text())
            if self.sz > 22:
                bl = True
        except BaseException as e:
            bl = True

        if bl:
            self.label.setText('''Wrong Size Entered.
Size set to Default(22)''')
            self.sz = 21

        else:
            self.sz -= 1

        # self.sz = int(self.sizeEdit.text())
        # self.popEdit.setText("9")
        self.pushButton.setEnabled(True)
        self.sizeEdit.setText(str(self.sz+1))
        self.sizeEdit.setReadOnly(True)
        self.popButton.setEnabled(True)
        self.topButton.setEnabled(True)
        self.sizeButton.setEnabled(False)

    def push(self):
        self.topEdit.setText("")
        self.label.setText("")
        self.popEdit.setText("")
        data = self.pushEdit.text().strip()

        if self.i == self.sz:
            self.label.setText("Queue is Full")
        elif data == "":
            self.label.setText("Please Enter a Valid Entry")
        else:
            self.i += 1
            # self.lineEdit_2.setText(str(ww.pop()))
            label_2 = QtWidgets.QLabel(self.centralwidget)
            label_2.setGeometry(QtCore.QRect(self.x-20, self.y, 21, 20))
            label_2.setAlignment(QtCore.Qt.AlignCenter)
            label_2.setObjectName("label_2")
            label_2.setText(str(self.i))
            label_2.show()

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

        if self.r == self.sz + 1:
            self.label.setText("Queue is Empty")
        else:
            z = self.ww[self.r]
            self.r += 1
            self.popEdit.setText(z.text())
            z.setText("")

            # z = self.ww.pop()
            # z.hide()
            # z.deleteLater()
            # self.i -= 1
            # self.y += self.p

    def top(self):
        self.pushEdit.setText("")
        self.popEdit.setText("")
        self.label.setText("")

        if self.r == self.sz + 1:
            self.label.setText("Queue is Empty")
        else:
            self.topEdit.setText(self.ww[self.r].text())


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
