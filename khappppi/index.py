###########################IMPORTING_LIBRARIES##########################################################################
from PyQt5.QtCore import *
from PyQt5.QtGui import *
# from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
import sys
import MySQLdb

from PyQt5.uic import loadUiType

ui, _ = loadUiType('pproject.ui')
login, _ = loadUiType('loginwindow.ui')
stack, _ = loadUiType('stack.ui')
queue, _ = loadUiType('queue.ui')
circqueue, _ = loadUiType('circQueue.ui')
deque, _ = loadUiType('deque.ui')
circdeque, _ = loadUiType('circdeque.ui')
linklist, _ = loadUiType('linkedlist.ui')


########################################################################################################################
#####################################ADDING_WINDOW_CLASSES##############################################################

################LINKLIST_CLASS##############

class Linkedlist(QMainWindow, linklist):

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
                self.label.setText("Index entered greater than number of nodes. Element inserted at end")
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
                self.ww[x].setText(self.ww[x + 1].text())

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
                self.label.setText("Index entered greater than number of nodes. End Element deleted")
                self.ww[self.i].setText("")

            else:
                for x in range(index, self.i - 1):
                    self.ww[x].setText(self.ww[x + 1].text())

                self.i -= 1
                self.ww[self.i].setText("")


#################################################################################################################
################CIRCULAR_DEQUE_CLASS##############

class CircDeque(QMainWindow, circdeque):

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
        self.pushButton_3.clicked.connect(self.clear)

    def clear(self):
        self.close()
        self.window7 = CircDeque()
        self.window7.show()
        # self.pushButton_8.autoClicked(self.open_queue_visualBox)

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


########################################################################################################################
######################DEQUE_CLASS#######################

class Deque(QMainWindow, deque):

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
            self.size()

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
        self.close()
        self.window6 = Deque()
        self.window6.show()

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
        if self.r == 0:
            self.label.setText("Deque is Full")
        elif data == "":
            self.label.setText("Please Enter a Valid Entry")
        else:
            if self.r == -1:
                self.r = 11
                self.i = 11
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

        if self.i == self.sz:
            self.label.setText("Deque is Full")
        elif data == "":
            self.label.setText("Please Enter a Valid Entry")
        else:
            if self.r == -1:
                self.r = 11
                self.i = 11
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
                self.i -= 1

        self.dec()

    def top(self):
        self.pushEdit.setText("")
        self.popEdit.setText("")
        self.topEdit_2.setText("")
        self.pushEdit_2.setText("")
        self.popEdit_2.setText("")
        self.label.setText("")

        if self.r == -1:
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


########################################################################################################################
######################CIRCULAR_QUEUE_CLASS#######################

class CircularQueue(QMainWindow, circqueue):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.setupUi(self)

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
            self.size()

    def handle_buttons(self):
        self.pushButton_2.clicked.connect(self.push_2)
        # self.popButton_2.clicked.connect(self.pop_2)
        self.topButton_2.clicked.connect(self.top_2)
        # self.sizeButton.clicked.connect(self.size)

        self.popButton.clicked.connect(self.pop)
        self.topButton.clicked.connect(self.top)
        # self.pushButton.clicked.connect(self.push)

        self.clearButton.clicked.connect(self.clear)

    def clear(self):
        self.close()
        self.window5 = CircularQueue()
        self.window5.show()

    def size(self):
        # self.sz = int(self.sizeEdit.text())
        # self.popEdit.setText("9")
        self.sizeEdit.setText("22")

        self.sizeEdit.setReadOnly(True)
        # self.pushButton.setEnabled(True)
        self.popButton.setEnabled(True)
        self.topButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        # self.popButton_2.setEnabled(True)
        self.topButton_2.setEnabled(True)
        self.sizeButton.setEnabled(False)

        self.dec()

    def push(self):
        self.topEdit_2.setText("")
        # self.popEdit_2.setText("")
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
        # self.popEdit_2.setText("")
        # self.pushEdit.setText("")
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
        # self.pushEdit.setText("")
        # self.popEdit_2.setText("")
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
        # self.pushEdit.setText("")
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
        # self.pushEdit.setText("")
        self.popEdit.setText("")
        self.topEdit_2.setText("")
        self.pushEdit_2.setText("")
        # self.popEdit_2.setText("")
        self.label.setText("")

        if self.i == -1:
            self.label.setText("Deque is Empty")
        else:
            self.topEdit.setText(self.ww[self.r].text())

        self.dec()

    def top_2(self):
        # self.pushEdit.setText("")
        self.popEdit.setText("")
        self.topEdit.setText("")
        self.pushEdit_2.setText("")
        # self.popEdit_2.setText("")
        self.label.setText("")

        if self.i == -1:
            self.label.setText("Deque is Empty")
        else:
            self.topEdit_2.setText(self.ww[self.i].text())

        self.dec()

    def dec(self):
        self.label_3.setText(str(self.r))
        self.label_5.setText(str(self.i))


########################################################################################################################
#########################QUEUE_CLASS############################

class Queue(QMainWindow, queue):

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
        self.close()
        self.window4 = Queue()
        self.window4.show()


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
        self.sizeEdit.setText(str(self.sz + 1))
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
            label_2.setGeometry(QtCore.QRect(self.x - 20, self.y, 21, 20))
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

        if self.r == self.i + 1:
            self.label.setText("Queue is Empty")
        else:
            z = self.ww[self.r]
            self.r += 1
            self.popEdit.setText(z.text())
            z.setText("")

    def top(self):
        self.pushEdit.setText("")
        self.popEdit.setText("")
        self.label.setText("")

        if self.r == self.i + 1:
            self.label.setText("Queue is Empty")
        else:
            self.topEdit.setText(self.ww[self.r].text())


########################################################################################################################
##########################STACK_CLASS############################
class Stack(QMainWindow, stack):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # global ww, i, s, x, y, p
        # i = 0
        # x, y, p = 490, 360, 30
        # ww = [1, 2, 3]
        self.ww = []
        self.ll = []
        self.i = -1
        self.x, self.y, self.p = 490, 444, 21
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
        self.close()
        self.window3 = Stack()
        self.window3.show()

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

        self.sizeEdit.setReadOnly(True)
        self.pushButton.setEnabled(True)
        self.popButton.setEnabled(True)
        self.sizeEdit.setText(str(self.sz + 1))
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

            z = self.ll.pop()
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


########################################################################################################################
###########################login_class###########################

class Login(QMainWindow, login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handle_login)
        self.pushButton_3.clicked.connect(self.Handle_signup)
        self.pushButton_2.clicked.connect(self.Handle_newuser)

    def Handle_login(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='hello@123#ty', db='visual_structures')
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        # confirmpassword=self.lineEdit_4.setReadOnly(True)
        confirmpassword = self.lineEdit_4.setEnabled(False)
        # email=self.lineEdit_3.setReadOnly(True)
        email = self.lineEdit_3.setEnabled(False)

        # sql = '''SELECT * FROM users where user_name = %s''', username

        sql = '''SELECT * FROM users '''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:

                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.setText('Invalid credentials')

    def Handle_newuser(self):
        confirmpassword = self.lineEdit_4.setEnabled(True)
        email = self.lineEdit_3.setEnabled(True)
        confirmpassword = self.lineEdit_4.text()
        email = self.lineEdit_3.text()

    def Handle_signup(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='hello@123#ty', db='visual_structures')
        self.cur = self.db.cursor()

        sql = '''SELECT * FROM users '''

        self.cur.execute(sql)
        data = self.cur.fetchall()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirmpassword = self.lineEdit_4.text()
        email = self.lineEdit_3.text()

        if username.strip() == '':
            self.label.setText('INValid Username')

        elif email.strip() == '' or '@' not in email:
            self.label.setText('INValid email id .Should contain @')

        elif password.strip() == '':
            self.label.setText('INValid Pass')

        elif confirmpassword.strip() == '':
            self.label.setText('INValid Confirm pass')

        elif confirmpassword != password:
            self.label.setText(' Confirm pass does not match pass')

        else:
            for row in data:
                if email == row[2] or username == row[1]:
                    self.label.setText('User Alredy Exist With this username or email')
                    break

            else:
                self.cur.execute('''
                    INSERT INTO users(user_name,user_email,user_password)
                     VALUES (%s, %s, %s)
                ''', (username, email, password))

                self.db.commit()
                self.label.setText("new user added")

                self.window2 = MainApp()
                self.close()
                self.window2.show()


########################################################################################################################
########################################################################################################################

####################MAINAPP_CLASS###############################
class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.user_id = -1
        self.email = ""
        self.username = ""
        self.Handle_Buttons()

    def Handle_UI_Changes(self):
        pass

    ########################################################################################################################

    def Handle_Buttons(self):
        ####################ICONS_BUTTONS#######################################

        self.introicon.clicked.connect(self.open_intro_tab)
        self.topicicon.clicked.connect(self.open_topics_tab)
        self.codesicon.clicked.connect(self.open_codes_tab)
        self.quizicon.clicked.connect(self.open_quiz_tab)
        self.loginicon.clicked.connect(self.open_login_tab)
        ###################LOGIN_TAB_BUTTONS#####################################
        self.pushButton_12.clicked.connect(self.Add_New_User)
        self.pushButton_13.clicked.connect(self.Login_user)
        self.pushButton_17.clicked.connect(self.Edit_User)
        ####################CODES_TAB_BUTTONS#####################################
        self.pushButton.clicked.connect(self.open_linklist_tab)
        self.pushButton_3.clicked.connect(self.open_stack_tab)
        self.pushButton_2.clicked.connect(self.open_queue_tab)

        self.pushButton_37.clicked.connect(self.back_main_topic_tab)
        self.pushButton_21.clicked.connect(self.back_main_topic_tab)
        self.pushButton_38.clicked.connect(self.back_main_topic_tab)
        ####################TOPICS_TAB_BUTTONS#####################################
        self.pushButton_18.clicked.connect(self.open_linklist_code_tab)
        self.pushButton_19.clicked.connect(self.open_stack_code_tab)
        self.pushButton_20.clicked.connect(self.open_queue_code_tab)

        self.pushButton_36.clicked.connect(self.back_main_tab)
        self.pushButton_35.clicked.connect(self.back_main_tab)
        self.pushButton_34.clicked.connect(self.back_main_tab)
        self.pushButton_33.clicked.connect(self.back_main_tab)
        self.pushButton_32.clicked.connect(self.back_main_tab)
        self.pushButton_51.clicked.connect(self.back_main_tab)

        #####################QUIZ_TAB_BUTTONS##########################################

        self.pushButton_4.clicked.connect(self.open_linklist_quiz_tab)
        self.pushButton_5.clicked.connect(self.open_stack_quiz_tab)
        self.pushButton_9.clicked.connect(self.open_queue_quiz_tab)

        self.pushButton_40.clicked.connect(self.next_linklist_quiz_tab)
        self.pushButton_44.clicked.connect(self.next_stack_quiz_tab)
        self.pushButton_48.clicked.connect(self.next_queue_quiz_tab)

        self.pushButton_39.clicked.connect(self.back_main_quiz_tab)
        self.pushButton_43.clicked.connect(self.back_main_quiz_tab)
        self.pushButton_47.clicked.connect(self.back_main_quiz_tab)
        self.pushButton_41.clicked.connect(self.back_linklist_quiz_tab)
        self.pushButton_45.clicked.connect(self.back_stack_quiz_tab)
        self.pushButton_49.clicked.connect(self.back_queue_quiz_tab)
        ######################QUIZ_TAB_OPTIONS_BUTTONS##################################
        ###########  LINKLIST  #################
        self.radioButton_2.clicked.connect(self.quiz_linklist_right_answers)
        self.radioButton.clicked.connect(self.quiz_linklist_wrong_answers)
        self.radioButton_3.clicked.connect(self.quiz_linklist_wrong_answers)
        self.radioButton_4.clicked.connect(self.quiz_linklist_wrong_answers)

        self.radioButton_7.clicked.connect(self.quiz_linklist_q2_right_answers)
        self.radioButton_5.clicked.connect(self.quiz_linklist_q2_wrong_answers)
        self.radioButton_6.clicked.connect(self.quiz_linklist_q2_wrong_answers)
        self.radioButton_8.clicked.connect(self.quiz_linklist_q2_wrong_answers)

        self.radioButton_27.clicked.connect(self.quiz_linklist_q3_right_answers)
        self.radioButton_25.clicked.connect(self.quiz_linklist_q3_wrong_answers)
        self.radioButton_28.clicked.connect(self.quiz_linklist_q3_wrong_answers)
        self.radioButton_31.clicked.connect(self.quiz_linklist_q3_wrong_answers)

        self.radioButton_29.clicked.connect(self.quiz_linklist_q4_right_answers)
        self.radioButton_32.clicked.connect(self.quiz_linklist_q4_wrong_answers)
        self.radioButton_30.clicked.connect(self.quiz_linklist_q4_wrong_answers)
        self.radioButton_26.clicked.connect(self.quiz_linklist_q4_wrong_answers)
        ############################################################################################
        ############### STACK  ####################
        self.radioButton_34.clicked.connect(self.quiz_stack_q1_right_answers)
        self.radioButton_35.clicked.connect(self.quiz_stack_q1_wrong_answers)
        self.radioButton_37.clicked.connect(self.quiz_stack_q1_wrong_answers)
        self.radioButton_38.clicked.connect(self.quiz_stack_q1_wrong_answers)

        self.radioButton_33.clicked.connect(self.quiz_stack_q2_right_answers)
        self.radioButton_36.clicked.connect(self.quiz_stack_q2_wrong_answers)
        self.radioButton_39.clicked.connect(self.quiz_stack_q2_wrong_answers)
        self.radioButton_40.clicked.connect(self.quiz_stack_q2_wrong_answers)

        self.radioButton_42.clicked.connect(self.quiz_stack_q3_right_answers)
        self.radioButton_43.clicked.connect(self.quiz_stack_q3_wrong_answers)
        self.radioButton_45.clicked.connect(self.quiz_stack_q3_wrong_answers)
        self.radioButton_46.clicked.connect(self.quiz_stack_q3_wrong_answers)

        self.radioButton_48.clicked.connect(self.quiz_stack_q4_right_answers)
        self.radioButton_41.clicked.connect(self.quiz_stack_q4_wrong_answers)
        self.radioButton_47.clicked.connect(self.quiz_stack_q4_wrong_answers)
        self.radioButton_44.clicked.connect(self.quiz_stack_q4_wrong_answers)
        ############################################################################################
        ############### QUEUE ###################
        self.radioButton_53.clicked.connect(self.quiz_queue_q1_right_answers)
        self.radioButton_55.clicked.connect(self.quiz_queue_q1_wrong_answers)
        self.radioButton_50.clicked.connect(self.quiz_queue_q1_wrong_answers)
        self.radioButton_52.clicked.connect(self.quiz_queue_q1_wrong_answers)

        self.radioButton_51.clicked.connect(self.quiz_queue_q2_right_answers)
        self.radioButton_54.clicked.connect(self.quiz_queue_q2_wrong_answers)
        self.radioButton_49.clicked.connect(self.quiz_queue_q2_wrong_answers)
        self.radioButton_56.clicked.connect(self.quiz_queue_q2_wrong_answers)

        self.radioButton_60.clicked.connect(self.quiz_queue_q3_right_answers)
        self.radioButton_61.clicked.connect(self.quiz_queue_q3_wrong_answers)
        self.radioButton_58.clicked.connect(self.quiz_queue_q3_wrong_answers)
        self.radioButton_63.clicked.connect(self.quiz_queue_q3_wrong_answers)

        self.radioButton_62.clicked.connect(self.quiz_queue_q4_right_answers)
        self.radioButton_59.clicked.connect(self.quiz_queue_q4_wrong_answers)
        self.radioButton_57.clicked.connect(self.quiz_queue_q4_wrong_answers)
        self.radioButton_64.clicked.connect(self.quiz_queue_q4_wrong_answers)

        #####################TOPICS_VISUALBOX_WINDOWS_BUTTONS###############################
        self.pushButton_7.clicked.connect(self.open_stack_visualBox)
        self.pushButton_8.clicked.connect(self.open_queue_visualBox)
        self.pushButton_6.clicked.connect(self.open_linklist_visualBox)

    ########################################################################################################################
    ############### FUNCTIONS_FOR_visual_windows ###########################################################################

    def open_stack_visualBox(self):
        self.window3 = Stack()
        self.window3.show()

    def open_queue_visualBox(self):
        x = self.comboBox_3.currentText()
        if x == "SINGLE QUEUE":
            self.window4 = Queue()
            self.window4.show()

        elif x == "DOUBLE ENDED QUEUE":
            self.window6 = Deque()
            self.window6.show()

        elif x == "CIRCULAR QUEUE":
            self.window5 = CircularQueue()
            self.window5.show()

        elif x == "CIRCULAR DEQUE":
            self.window7 = CircDeque()
            self.window7.show()

    def open_linklist_visualBox(self):
        self.window8 = Linkedlist()
        self.window8.show()

    #########################################################################
    ####################open_MAIN_tabs############################################

    def open_intro_tab(self):
        self.outertabWidget.setCurrentIndex(0)

    def open_topics_tab(self):
        self.outertabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)

    def open_codes_tab(self):
        self.outertabWidget.setCurrentIndex(2)
        self.tabWidget_3.setCurrentIndex(0)

    def open_quiz_tab(self):
        self.outertabWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)
        self.clear_answers()

    def open_login_tab(self):
        self.outertabWidget.setCurrentIndex(4)

    ############################################################################
    ################open_back_code_tabs#########################################

    def open_linklist_tab(self):
        self.tabWidget_3.setCurrentIndex(1)

    def open_stack_tab(self):
        self.tabWidget_3.setCurrentIndex(2)

    def open_queue_tab(self):
        self.tabWidget_3.setCurrentIndex(3)

    def back_main_topic_tab(self):
        self.tabWidget_3.setCurrentIndex(0)

    ############################################################################
    ################open_back_topics_tabs########################################

    def open_linklist_code_tab(self):
        self.tabWidget_2.setCurrentIndex(1)

    def open_stack_code_tab(self):
        self.tabWidget_2.setCurrentIndex(2)

    def open_queue_code_tab(self):
        x = self.comboBox_3.currentText()
        if x == "SINGLE QUEUE":
            self.tabWidget_2.setCurrentIndex(3)

        elif x == "DOUBLE ENDED QUEUE":
            self.tabWidget_2.setCurrentIndex(4)

        elif x == "CIRCULAR QUEUE":
            self.tabWidget_2.setCurrentIndex(5)

        elif x == "CIRCULAR DEQUE":
            self.tabWidget_2.setCurrentIndex(6)

    def back_main_tab(self):
        self.tabWidget_2.setCurrentIndex(0)

    ############################################################################
    ################open_back_next_quiz_tabs####################################

    def open_linklist_quiz_tab(self):
        self.tabWidget.setCurrentIndex(1)
        self.clear_answers()

    def open_stack_quiz_tab(self):
        self.tabWidget.setCurrentIndex(3)
        self.clear_answers()

    def open_queue_quiz_tab(self):
        self.tabWidget.setCurrentIndex(5)
        self.clear_answers()

    def next_linklist_quiz_tab(self):
        self.tabWidget.setCurrentIndex(2)
        self.clear_answers()

    def next_stack_quiz_tab(self):
        self.tabWidget.setCurrentIndex(4)
        self.clear_answers()

    def next_queue_quiz_tab(self):
        self.tabWidget.setCurrentIndex(6)
        self.clear_answers()

    def back_main_quiz_tab(self):
        self.tabWidget.setCurrentIndex(0)
        self.clear_answers()

    def back_linklist_quiz_tab(self):
        self.tabWidget.setCurrentIndex(1)
        self.clear_answers()

    def back_stack_quiz_tab(self):
        self.tabWidget.setCurrentIndex(3)
        self.clear_answers()

    def back_queue_quiz_tab(self):
        self.tabWidget.setCurrentIndex(5)
        self.clear_answers()

    #########################################################################
    #################quiz_answers############################################

    def quiz_linklist_right_answers(self):
        self.label_7.setText('CORRECT')

    def quiz_linklist_wrong_answers(self):
        self.label_7.setText('WRONG')

    def quiz_linklist_q2_right_answers(self):
        self.label_8.setText('CORRECT')

    def quiz_linklist_q2_wrong_answers(self):
        self.label_8.setText('WRONG')

    def quiz_linklist_q3_right_answers(self):
        self.label_20.setText('CORRECT')

    def quiz_linklist_q3_wrong_answers(self):
        self.label_20.setText('WRONG')

    def quiz_linklist_q4_right_answers(self):
        self.label_21.setText('CORRECT')

    def quiz_linklist_q4_wrong_answers(self):
        self.label_21.setText('WRONG')

    ################################################################################
    def quiz_stack_q1_right_answers(self):
        self.label_22.setText('CORRECT')

    def quiz_stack_q1_wrong_answers(self):
        self.label_22.setText('WRONG')

    def quiz_stack_q2_right_answers(self):
        self.label_23.setText('CORRECT')

    def quiz_stack_q2_wrong_answers(self):
        self.label_23.setText('WRONG')

    def quiz_stack_q3_right_answers(self):
        self.label_24.setText('CORRECT')

    def quiz_stack_q3_wrong_answers(self):
        self.label_24.setText('WRONG')

    def quiz_stack_q4_right_answers(self):
        self.label_25.setText('CORRECT')

    def quiz_stack_q4_wrong_answers(self):
        self.label_25.setText('WRONG')

    #########################################################################
    def quiz_queue_q1_right_answers(self):
        self.label_26.setText('CORRECT')

    def quiz_queue_q1_wrong_answers(self):
        self.label_26.setText('WRONG')

    def quiz_queue_q2_right_answers(self):
        self.label_27.setText('CORRECT')

    def quiz_queue_q2_wrong_answers(self):
        self.label_27.setText('WRONG')

    def quiz_queue_q3_right_answers(self):
        self.label_28.setText('CORRECT')

    def quiz_queue_q3_wrong_answers(self):
        self.label_28.setText('WRONG')

    def quiz_queue_q4_right_answers(self):
        self.label_29.setText('CORRECT')

    def quiz_queue_q4_wrong_answers(self):
        self.label_29.setText('WRONG')

###############################fxn to clear answer####################
    def clear_answers(self):

        self.label_7.setText('')
        self.label_8.setText('')
        self.label_20.setText('')
        self.label_21.setText('')
        self.label_22.setText('')
        self.label_23.setText('')
        self.label_24.setText('')
        self.label_25.setText('')
        self.label_26.setText('')
        self.label_27.setText('')
        self.label_28.setText('')
        self.label_29.setText('')

    ##########################################################################
    ###############database_users#############################################

    def Add_New_User(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='hello@123#ty', db='visual_structures')
        self.cur = self.db.cursor()

        sql = '''SELECT * FROM users '''

        self.cur.execute(sql)
        data = self.cur.fetchall()

        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        confirmpassword = self.lineEdit_4.text()

        if username.strip() == '':
            self.label_6.setText('INValid Username')

        elif email.strip() == '' or '@' not in email:
            self.label_6.setText('INValid email id .Should contain @')

        elif password.strip() == '':
            self.label_6.setText('INValid Pass')

        elif confirmpassword.strip() == '':
            self.label_6.setText('INValid Confirm pass')

        elif confirmpassword != password:
            self.label_6.setText(' Confirm pass does not match pass')

        else:
            for row in data:
                if email == row[2] or username == row[1]:
                    self.statusBar().showMessage("USER ALREADY EXISTS WITH THIS EMAIL OR USERNAME")
                    break

            else:
                self.label_6.setText('')
                self.cur.execute('''
                        INSERT INTO users(user_name,user_email,user_password)
                        VALUES (%s, %s, %s)
                ''', (username, email, password))

                self.db.commit()
                self.statusBar().showMessage("new user added")

            self.lineEdit_2.setText("")
            self.lineEdit.setText("")

        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")

    def Login_user(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='hello@123#ty', db='visual_structures')
        self.cur = self.db.cursor()

        username = self.lineEdit_9.text()
        password = self.lineEdit_10.text()

        # sql = '''SELECT * FROM users where user_name = %s''', username

        sql = '''SELECT * FROM users '''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:
                # print('user match')
                self.statusBar().showMessage('Valid Username & Password')
                self.groupBox_4.setEnabled(True)

                self.user_id = row[0]
                self.email = row[2]
                self.username = row[1]
                self.lineEdit_20.setText(row[1])
                self.lineEdit_19.setText(row[2])
                self.lineEdit_18.setText(row[3])
                break
        else:
            self.statusBar().showMessage("Invalid login details")

    def Edit_User(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='hello@123#ty', db='visual_structures')
        self.cur = self.db.cursor()

        sql = '''SELECT * FROM users '''

        self.cur.execute(sql)
        data = self.cur.fetchall()

        username = self.lineEdit_20.text()
        email = self.lineEdit_19.text()
        password = self.lineEdit_18.text()
        confirmpassword = self.lineEdit_17.text()

        if username.strip() == '':
            self.label_6.setText('INValid Username')

        elif email.strip() == '' or '@' not in email:
            self.label_6.setText('INValid email id .Should contain @')

        elif password.strip() == '':
            self.label_6.setText('INValid Pass')

        elif confirmpassword.strip() == '':
            self.label_6.setText('INValid Confirm pass')

        elif confirmpassword != password:
            self.label_6.setText(' Confirm pass does not match pass')

        else:
            for row in data:
                if email != self.email or username != self.username:
                    if email == row[2] or username == row[1]:
                        self.statusBar().showMessage("A USER ALREADY EXISTS WITH THIS EMAIL OR USERNAME")
                        break

            else:
                if password == confirmpassword:
                    self.cur.execute('''
                         UPDATE users SET user_name = %s, user_email = %s, user_password=%s WHERE user_id=%s
                    ''', (username, email, password, self.user_id))

                    self.db.commit()
                    self.statusBar().showMessage('user data updates successfully')

                else:
                    self.statusBar().showMesssage('make sure you entered password correctly')

                username = self.lineEdit_9.setText('')
                password = self.lineEdit_10.setText('')

                username = self.lineEdit_20.setText('')
                email = self.lineEdit_19.setText('')
                password = self.lineEdit_18.setText('')
                confirmpassword = self.lineEdit_17.setText('')

                self.groupBox_4.setEnabled(False)


def main():
    app = QApplication(sys.argv)
    # window = Login()                                                      #########################
    window = MainApp()
    window.show()                                                          #######################
    app.exec_()


if __name__ == '__main__':
    main()
