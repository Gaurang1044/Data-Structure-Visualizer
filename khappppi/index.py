from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb

from PyQt5.uic import loadUiType

ui, _ = loadUiType('pproject.ui')
login,_ = loadUiType('loginwindow.ui')

class Login(QMainWindow , login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handle_login)
        # self.Handle_login()

    def Handle_login(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='hello@123#ty', db='visual_structures')
        self.cur = self.db.cursor()

        username= self.lineEdit.text()
        password=self.lineEdit_2.text()

        # sql = '''SELECT * FROM users where user_name = %s''', username

        sql = '''SELECT * FROM users '''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:
                print('user match')
                self.window2=MainApp()
                self.close()
                self.window2.show()

            else:
                self.label.setText('Invalid credentials')


class MainApp(QMainWindow, ui):
    user_id=0
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
        self.pushButton_13.clicked.connect(self.Login_user)
        self.pushButton_17.clicked.connect(self.Edit_User)

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
        self.db = MySQLdb.connect(host='localhost', user='root', password='hello@123#ty', db='visual_structures')
        self.cur = self.db.cursor()

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
            self.label_6.setText('')
            self.cur.execute('''
                         INSERT INTO users(user_name,user_email,user_password)
                         VALUES (%s, %s, %s)
                     ''', (username, email, password))

            self.db.commit()
            self.statusBar().showMessage("new user added")

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
            if username==row[1] and password == row[3]:
                print('user match')
                self.statusBar().showMessage('Valid Username & Password')
                self.groupBox_4.setEnabled(True)

                MainApp.user_id=row[0]
                self.lineEdit_20.setText(row[1])
                self.lineEdit_19.setText(row[2])
                self.lineEdit_18.setText(row[3])
                break
        else:
            self.statusBar().showMessage("Invalid login details")

    def Edit_User(self):

        username = self.lineEdit_20.text()
        email = self.lineEdit_19.text()
        password = self.lineEdit_18.text()
        confirmpassword = self.lineEdit_17.text()


        if password == confirmpassword:
            self.db = MySQLdb.connect(host='localhost', user='root', password='hello@123#ty', db='visual_structures')
            self.cur = self.db.cursor()

            self.cur.execute('''
                 UPDATE users SET user_name = %s, user_email = %s, user_password=%s WHERE user_id=%s
            ''', (username, email, password, MainApp.user_id))

            self.db.commit()
            self.statusBar().showMessage('user data updates sucessfully')

        else:
            print('make sure you entered password correctly')


def main():
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
