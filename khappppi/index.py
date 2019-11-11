from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb

from PyQt5.uic import loadUiType

ui,_ = loadUiType('pproject.ui')

class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_UI_Changes(self):
        pass

    def Handle_Buttons(self):
        self.introicon.clicked.connect(self.open_intro_tab)
        self.topicicon.clicked.connect(self.open_topics_tab)
        self.codesicon.clicked.connect(self.open_codes_tab)
        self.quizicon.clicked.connect(self.open_quiz_tab)
        self.loginicon.clicked.connect(self.open_login_tab)

        self.pushButton_12.clicked.connect(self.Add_New_User)
#########################################################################
####################open_tabs############################################

    def open_intro_tab(self):
        self.outertabWidget.setCurrentIndex(0)

    def open_topics_tab(self):
        self.outertabWidget.setCurrentIndex(1)

    def open_codes_tab(self):
        self.outertabWidget.setCurrentIndex(2)

    def open_quiz_tab(self):
        self.outertabWidget.setCurrentIndex(3)

    def open_login_tab(self):
        self.outertabWidget.setCurrentIndex(4)

###############################################################
############database_users#####################################

    def Add_New_User(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='AaBb1234', db='visual_structures')
        self.cur = self.db.cursor()

        username = self.lineEdit.text()
        email = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        confirmpassword = self.lineEdit_4.text()

        if password == confirmpassword:
            self.cur.execute('''
                INSERT INTO users(user_name,user_email,user_password)
                VALUES (%s, %s, %s)
            ''' , (username, email, password))

            self.db.commit()
            self.statusBar().showMessage("new user added")

        else:
            pass

    def Login_user(self):
        pass

    def Edit_User(self):
        pass


def main():
    app= QApplication(sys.argv)
    window= MainApp()
    window.show()
    app.exec_()

if __name__ =='__main__':
    main()