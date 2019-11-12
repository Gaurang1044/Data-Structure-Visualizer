# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'queue.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(160, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pushEdit.setGeometry(QtCore.QRect(20, 50, 113, 20))
        self.pushEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pushEdit.setObjectName("pushEdit")
        self.popButton = QtWidgets.QPushButton(self.centralwidget)
        self.popButton.setEnabled(False)
        self.popButton.setGeometry(QtCore.QRect(160, 100, 75, 23))
        self.popButton.setObjectName("popButton")
        self.popEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.popEdit.setGeometry(QtCore.QRect(20, 100, 113, 20))
        self.popEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.popEdit.setReadOnly(True)
        self.popEdit.setObjectName("popEdit")
        self.topEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.topEdit.setGeometry(QtCore.QRect(20, 150, 113, 20))
        self.topEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.topEdit.setReadOnly(True)
        self.topEdit.setObjectName("topEdit")
        self.topButton = QtWidgets.QPushButton(self.centralwidget)
        self.topButton.setEnabled(False)
        self.topButton.setGeometry(QtCore.QRect(160, 150, 75, 23))
        self.topButton.setObjectName("topButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 253, 151, 20))
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 320, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.sizeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sizeEdit.setEnabled(True)
        self.sizeEdit.setGeometry(QtCore.QRect(20, 10, 113, 20))
        self.sizeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.sizeEdit.setReadOnly(False)
        self.sizeEdit.setObjectName("sizeEdit")
        self.sizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.sizeButton.setGeometry(QtCore.QRect(160, 10, 75, 23))
        self.sizeButton.setObjectName("sizeButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 383, 21, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Enqueue"))
        self.popButton.setText(_translate("MainWindow", "Dequeue"))
        self.topButton.setText(_translate("MainWindow", "Front"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.sizeEdit.setPlaceholderText(_translate("MainWindow", "Max size : 21"))
        self.sizeButton.setText(_translate("MainWindow", "Size"))
        self.label_2.setText(_translate("MainWindow", "21"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
