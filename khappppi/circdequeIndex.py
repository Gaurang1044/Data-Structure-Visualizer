from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType

ui, _ = loadUiType('circdeque.ui')


# global ww, i, s, x, y, p
# i = 0
# x, y, p = 490, 360, 30
# ww = [1, 2, 3]


class MainApp(QMainWindow, ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ww = []
        self.ll = []
        self.i = -1
        self.r = -1
        self.x, self.y, self.z, self.p = 490, 440, 440, 21
        self.s = "gLineEdit"
        self.sz = 21

        self.set_boxes()
        self.handle_buttons()
        self.size()

    def set_boxes(self):

        for x in range(0, 22):
            label_2 = QtWidgets.QLabel(self.centralwidget)
            label_2.setGeometry(QtCore.QRect(self.x - 20, self.y, 21, 20))
            label_2.setAlignment(QtCore.Qt.AlignCenter)
            label_2.setObjectName("label_2")
            label_2.setText(str(x))
            label_2.hide()
            self.ll.append(label_2)

            line_editt = QtWidgets.QLineEdit(self.centralwidget)
            line_editt.setGeometry(QtCore.QRect(self.x, self.y, 113, 20))
            line_editt.setAlignment(QtCore.Qt.AlignCenter)
            line_editt.setReadOnly(True)
            # line_editt.setText(data)
            line_editt.setObjectName(self.s + str(x))
            line_editt.hide()
            self.ww.append(line_editt)
            self.y = self.y - self.p

    def handle_buttons(self):
        self.pushButton_2.clicked.connect(self.push_2)
        self.popButton_2.clicked.connect(self.pop_2)
        self.topButton_2.clicked.connect(self.top_2)
        # self.sizeButton.clicked.connect(self.size)

        self.popButton.clicked.connect(self.pop)
        self.topButton.clicked.connect(self.top)
        self.pushButton.clicked.connect(self.push)
        self.clearButton.clicked.connect(self.clear)

    def clear(self):
        pass

    def size(self):
        # self.sz = int(self.sizeEdit.text())
        # self.popEdit.setText("9")
        self.sizeEdit.setReadOnly(True)
        self.sizeEdit.setText("22")
        self.pushButton.setEnabled(True)
        self.popButton.setEnabled(True)
        self.topButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.popButton_2.setEnabled(True)
        self.topButton_2.setEnabled(True)
        self.sizeButton.setEnabled(False)

        self.dec()

    def push(self):
        self.topEdit_2.setText("")
        self.popEdit_2.setText("")
        self.pushEdit_2.setText("")
        self.topEdit.setText("")
        self.label.setText("")
        self.popEdit.setText("")

        data = self.pushEdit.text().strip()
        if (self.i == self.sz and self.r == 0) or (self.r == self.i + 1):
            self.label.setText("Deque is Full")
        elif data == "":
            self.label.setText("Please Enter a Valid Entry")
        else:
            if self.r == -1:
                self.r = 0
                self.i = 0
            else:
                if self.r == 0:
                    self.r = self.sz
                else:
                    self.r -= 1
            self.ww[self.r].show()
            self.ww[self.r].setText(data)
            self.ll[self.r].show()

        self.dec()

    def push_2(self):
        self.topEdit_2.setText("")
        self.popEdit_2.setText("")
        self.pushEdit.setText("")
        self.topEdit.setText("")
        self.label.setText("")
        self.popEdit.setText("")

        data = self.pushEdit_2.text().strip()

        if (self.i == self.sz and self.r == 0) or (self.r == self.i + 1):
            self.label.setText("Stack is Full")
        elif data == "":
            self.label.setText("Please Enter a Valid Entry")
        else:
            if self.r == -1:
                self.r = 0
                self.i = 0
            else:
                if self.i == self.sz:
                    self.i = 0
                else:
                    self.i += 1

            self.ww[self.i].show()
            self.ww[self.i].setText(data)
            self.ll[self.i].show()

        self.dec()

    def pop(self):
        self.topEdit_2.setText("")
        self.pushEdit_2.setText("")
        self.topEdit.setText("")
        self.pushEdit.setText("")
        self.popEdit_2.setText("")
        self.label.setText("")

        if self.r == -1:
            self.label.setText("Queue is Empty")
        else:

            self.popEdit.setText(self.ww[self.r].text())
            self.ww[self.r].setText("")
            self.ww[self.r].hide()
            self.ll[self.r].hide()

            if self.i == self.r:
                self.i = -1
                self.r = -1
            else:
                if self.r == self.sz:
                    self.r = 0
                else:
                    self.r += 1

        self.dec()

    def pop_2(self):
        self.topEdit_2.setText("")
        self.pushEdit_2.setText("")
        self.topEdit.setText("")
        self.pushEdit.setText("")
        self.popEdit.setText("")
        self.label.setText("")

        if self.r == -1:
            self.label.setText("Queue is Empty")
        else:

            self.popEdit_2.setText(self.ww[self.i].text())
            self.ww[self.i].setText("")
            self.ww[self.i].hide()
            self.ll[self.i].hide()

            if self.i == self.r:
                self.i = -1
                self.r = -1
            else:
                if self.i == 0:
                    self.i = self.sz
                else:
                    self.i -= 1

        self.dec()

    def top(self):
        self.pushEdit.setText("")
        self.popEdit.setText("")
        self.topEdit_2.setText("")
        self.pushEdit_2.setText("")
        self.popEdit_2.setText("")
        self.label.setText("")

        if self.i == -1:
            self.label.setText("Deque is Empty")
        else:
            self.topEdit.setText(self.ww[self.r].text())

        self.dec()

    def top_2(self):
        self.pushEdit.setText("")
        self.popEdit.setText("")
        self.topEdit.setText("")
        self.pushEdit_2.setText("")
        self.popEdit_2.setText("")
        self.label.setText("")

        if self.i == -1:
            self.label.setText("Deque is Empty")
        else:
            self.topEdit_2.setText(self.ww[self.i].text())

        self.dec()

    def dec(self):
        self.label_3.setText(str(self.r))
        self.label_5.setText(str(self.i))


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
