import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from QtGui import Ui_MainWindow
import time
import requests
import urllib3
from lcu_driver import Connector
import webbrowser
import os
import subprocess
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        #run tool
        self.uic.start_button.clicked.connect(self.bdtool)
        #stop tool
        self.uic.stop_button.clicked.connect(self.tdtool)
        #Support
        self.uic.email.clicked.connect(self.email)
        self.uic.Facebook.clicked.connect(self.facebook)
        #toiuu
        self.uic.reset_tool.clicked.connect(self.reset)
        self.uic.tt_edit.setText('Đang rảnh')
    def zalo(self):
        webbrowser.open("",new=0, autoraise=True)
    def facebook(self):
        webbrowser.open("https://www.facebook.com/PhCtrlZ/",new=0, autoraise=True)
    def email(self):
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=CllgCJqZhJhVlHrkMQNKWgfchBdZSDKqrtDgTPLFKvTHRszsLjbtMMbtLCJmXzKPkjlvBbWMkCg",new=0, autoraise=True)
    def bdtool(self):
        path="picks.txt"
        os.remove(path)
        path2="bans.txt"
        os.remove(path2)
        self.uic.tt_edit.setText('đang trọng trạng thái pick tướng')
        a=self.uic.pick_edit.toPlainText()  
        b=self.uic.pick_edit2.toPlainText()
        c=self.uic.pick_edit3.toPlainText()
        d=self.uic.pick_edit4.toPlainText()
        e=self.uic.pick_edit5.toPlainText()
        f=self.uic.ban_edit.toPlainText()
        g=self.uic.ban_edit1.toPlainText()
        h=self.uic.ban_edit2.toPlainText()
        i=self.uic.ban_edit3.toPlainText()
        j=self.uic.ban_edit4.toPlainText()
        with open("picks.txt", "a",encoding="utf-8") as file:
            file.writelines(a+"\n")
        with open("picks.txt", "a",encoding="utf-8") as file:
            file.writelines(b+"\n")
        with open("picks.txt", "a",encoding="utf-8") as file:
            file.writelines(c+"\n")
        with open("picks.txt", "a",encoding="utf-8") as file:
            file.writelines(d+"\n") 
        with open("picks.txt", "a",encoding="utf-8") as file:
            file.writelines(e+"\n")    

        with open("bans.txt","a",encoding="utf-8") as file:
            file.writelines(f+"\n")
        with open("bans.txt","a",encoding="utf-8") as file:
            file.writelines(g+"\n")
        with open("bans.txt","a",encoding="utf-8") as file:
            file.writelines(h+"\n")
        with open("bans.txt","a",encoding="utf-8") as file:
            file.writelines(i+"\n")
        with open("bans.txt","a",encoding="utf-8") as file:
            file.writelines(j+"\n")
        os.startfile("driver.exe")
        self.uic.tt_edit.setText('Setup thành công vô game đi!!!')
    def tdtool(self):
        self.uic.tt_edit.setText('Đã tạm dừng')
        os.system("taskkill /F /im driver.exe")
        pass
    def reset(self):
        self.uic.tt_edit.setText('Successfully!!!')

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())