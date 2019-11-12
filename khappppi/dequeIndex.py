from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType

ui, _ = loadUiType('deque.ui')

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
        self.x, self.y,self.z, self.p = 490, 440, 440, 21
        self.s = "gLineEdit"
        self.sz = 21

        self.handle_buttons()

    def handle_buttons(self):
        self.pushButton_2.clicked.connect(self.push_2)
        self.popButton_2.clicked.connect(self.pop_2)
        self.topButton_2.clicked.connect(self.top_2)
        self.sizeButton.clicked.connect(self.size)


        self.popButton.clicked.connect(self.pop)
        self.topButton.clicked.connect(self.top)
        self.pushButton.clicked.connect(self.push)


    def size(self):
        # self.sz = int(self.sizeEdit.text())
        # self.popEdit.setText("9")
        self.sizeEdit.setReadOnly(True)
        self.pushButton.setEnabled(True)
        self.popButton.setEnabled(True)
        self.topButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.popButton_2.setEnabled(True)
        self.topButton_2.setEnabled(True)
        self.sizeButton.setEnabled(False)

    def push(self):
        self.topEdit_2.setText("")
        self.popEdit_2.setText("")
        self.pushEdit_2.setText("")
        self.topEdit.setText("")
        self.label.setText("")
        self.popEdit.setText("")

        data = self.pushEdit.text().strip()
        if self.r == -1:
            self.label.setText("Deque is Full")
        elif data == "":
            self.label.setText("Please Enter a Valid Entry")
        else:
            self.r -= 1
            label_2 = QtWidgets.QLabel(self.centralwidget)
            label_2.setGeometry(QtCore.QRect(self.x - 20, self.z, 21, 20))
            label_2.setAlignment(QtCore.Qt.AlignCenter)
            label_2.setObjectName("label_2")
            label_2.setText(str(self.r))
            label_2.show()
            self.ll.append(label_2)

            line_editt = QtWidgets.QLineEdit(self.centralwidget)
            line_editt.setGeometry(QtCore.QRect(self.x, self.z, 113, 20))
            line_editt.setAlignment(QtCore.Qt.AlignCenter)
            line_editt.setReadOnly(True)
            line_editt.setText(data)
            line_editt.setObjectName(self.s + str(self.r))
            line_editt.show()
            self.ww.append(line_editt)
            self.z = self.z + self.p

    def push_2(self):
        self.topEdit_2.setText("")
        self.popEdit_2.setText("")
        self.pushEdit.setText("")
        self.topEdit.setText("")
        self.label.setText("")
        self.popEdit.setText("")

        data = self.pushEdit_2.text().strip()

        if self.i == self.sz:
            self.label.setText("Stack is Full")
        elif data == "":
            self.label.setText("Please Enter a Valid Entry")
        else:
            self.i += 1
            # self.lineEdit_2.setText(str(ww.pop()))

            label_2 = QtWidgets.QLabel(self.centralwidget)
            label_2.setGeometry(QtCore.QRect(self.x - 20, self.y, 21, 20))
            label_2.setAlignment(QtCore.Qt.AlignCenter)
            label_2.setObjectName("label_2")
            label_2.setText(str(self.i))
            label_2.show()
            self.ll.append(label_2)

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
        self.topEdit_2.setText("")
        self.pushEdit_2.setText("")
        self.topEdit.setText("")
        self.pushEdit.setText("")
        self.popEdit_2.setText("")
        self.label.setText("")

        if self.r == self.i:
            self.label.setText("Queue is Empty")
        else:
            z = self.ww[self.r]
            self.ww[self.r] = 0
            self.popEdit.setText(z.text())
            z.setText("")
            z.hide()
            z.deleteLater()

            z = self.ll[self.r]
            self.ll[self.r] = 0
            z.hide()
            z.deleteLater()

            self.r += 1

            # z = self.ww.pop()
            # self.i -= 1
            self.z -= self.p

    def pop_2(self):
        self.topEdit_2.setText("")
        self.pushEdit_2.setText("")
        self.topEdit.setText("")
        self.pushEdit.setText("")
        self.popEdit.setText("")
        self.label.setText("")

        if self.i == -1:
            self.label.setText("Deque is Empty")
        else:
            z = self.ww.pop()
            self.popEdit_2.setText(z.text())
            z.hide()
            z.deleteLater()

            z = self.ll.pop()
            z.hide()
            z.deleteLater()

            self.i -= 1
            self.y += self.p

    def top(self):
        self.pushEdit.setText("")
        self.popEdit.setText("")
        self.topEdit_2.setText("")
        self.pushEdit_2.setText("")
        self.popEdit_2.setText("")
        self.label.setText("")

        if self.r == self.i:
            self.label.setText("Deque is Empty")
        else:
            self.topEdit.setText(self.ww[self.r].text())





    def top_2(self):
        self.pushEdit.setText("")
        self.popEdit.setText("")
        self.topEdit.setText("")
        self.pushEdit_2.setText("")
        self.popEdit_2.setText("")
        self.label.setText("")

        if self.i == self.r:
            self.label.setText("Deque is Empty")
        else:
            self.topEdit_2.setText(self.ww[self.i].text())


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
