from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType

ui, _ = loadUiType('linkedlist.ui')


class MainApp(QMainWindow, ui):

    def __init__(self):

        QMainWindow.__init__(self)
        self.setupUi(self)
        self.i = 0
        self.sz = 15
        self.ww = []
        self.initialiseList()
        self.handle_buttons()

    def handle_buttons(self):
        self.pushButton.clicked.connect(self.instAtFront)
        self.pushButton_2.clicked.connect(self.instAtEnd)
        self.pushButton_3.clicked.connect(self.instAtIndex)
        self.pushButton_4.clicked.connect(self.delFront)
        self.pushButton_5.clicked.connect(self.delEnd)
        self.pushButton_6.clicked.connect(self.delIndex)

    def initialiseList(self):
        self.ww.append(self.lineEdit)
        self.ww.append(self.lineEdit_2)
        self.ww.append(self.lineEdit_12)
        self.ww.append(self.lineEdit_13)
        self.ww.append(self.lineEdit_14)
        self.ww.append(self.lineEdit_15)
        self.ww.append(self.lineEdit_16)
        self.ww.append(self.lineEdit_17)
        self.ww.append(self.lineEdit_18)
        self.ww.append(self.lineEdit_19)
        self.ww.append(self.lineEdit_3)
        self.ww.append(self.lineEdit_21)
        self.ww.append(self.lineEdit_23)
        self.ww.append(self.lineEdit_20)
        self.ww.append(self.lineEdit_22)

    def clearText(self):
        self.label.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_24.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")

    def instAtFront(self):
        data = self.lineEdit_4.text().strip()
        self.clearText()
        self.lineEdit_4.setText(data)

        if self.i == self.sz:
            self.label.setText("Linked List is Full")
        elif data == "":
            self.label.setText("Please Enter a Valid Entry")
        else:
            # self.label.setText(str(self.i))

            for x in range(0, self.i + 1):
                p = self.ww[x].text()
                self.ww[x].setText(data)
                data = p
            self.i += 1

    def instAtEnd(self):
        data = self.lineEdit_24.text().strip()
        self.clearText()
        self.lineEdit_24.setText(data)

        if self.i == self.sz:
            self.label.setText("Linked List is Full")
        elif data == "":
            self.label.setText("Please Enter a Valid Entry")
        else:
            # self.label.setText(str(self.i))
            self.ww[self.i].setText(data)
            self.i += 1

    def instAtIndex(self):

        data = self.lineEdit_6.text().strip()
        index = self.lineEdit_10.text().strip()
        self.clearText()
        self.lineEdit_6.setText(data)
        self.lineEdit_10.setText(index)

        bl = False

        try:
            index = int(index)
            if index > 14:
                bl = True
        except BaseException as e:
            bl = True

        if self.i == self.sz:
            self.label.setText("Linked List is Full")
        elif data == "":
            self.label.setText("Please Enter a Valid Data Entry")
        elif bl:
            self.label.setText("Please Enter a Valid Index less than 14")
        else:
            if index > self.i:
                self.ww[self.i].setText(data)
                self.i += 1
            else:
                for x in range(index, self.i + 1):
                    p = self.ww[x].text()
                    self.ww[x].setText(data)
                    data = p
                self.i += 1

            # self.label.setText(str(self.i))

    def delFront(self):
        self.clearText()
        if self.i == 0:
            self.label.setText("Linked List is Empty")
        else:
            self.lineEdit_7.setText(self.ww[0].text())
            for x in range(0, self.i - 1):
                self.ww[x].setText(self.ww[x+1].text())

            self.i -= 1
            self.ww[self.i].setText("")

    def delEnd(self):
        self.clearText()

        if self.i == 0:
            self.label.setText("Linked List is Empty")
        else:
            self.i -= 1
            self.lineEdit_8.setText(self.ww[self.i].text())
            self.ww[self.i].setText("")

    def delIndex(self):

        index = self.lineEdit_9.text().strip()
        self.clearText()
        self.lineEdit_9.setText(index)

        bl = False

        try:
            index = int(index)
            if index > 14:
                bl = True
        except BaseException as e:
            bl = True

        if self.i == 0:
            self.label.setText("Linked List is Empty")
        elif bl:
            self.label.setText("Please Enter a Valid Index less than 14")
        else:
            if index > self.i:
                self.i -= 1
                # self.lineEdit_9.setText(self.ww[self.i].text())
                self.ww[self.i].setText("")

            else:
                for x in range(index, self.i - 1):
                    self.ww[x].setText(self.ww[x + 1].text())

                self.i -= 1
                self.ww[self.i].setText("")


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
