# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 282)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 581, 231))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tt_edit = QtWidgets.QLineEdit(self.tab)
        self.tt_edit.setGeometry(QtCore.QRect(100, 100, 171, 20))
        self.tt_edit.setText("")
        self.tt_edit.setObjectName("tt_edit")
        self.start_button = QtWidgets.QPushButton(self.tab)
        self.start_button.setGeometry(QtCore.QRect(0, 140, 75, 23))
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.tab)
        self.stop_button.setGeometry(QtCore.QRect(90, 140, 75, 23))
        self.stop_button.setObjectName("stop_button")
        self.pick_edit = QtWidgets.QTextEdit(self.tab)
        self.pick_edit.setGeometry(QtCore.QRect(120, 10, 71, 31))
        self.pick_edit.setObjectName("pick_edit")
        self.pick_edit2 = QtWidgets.QTextEdit(self.tab)
        self.pick_edit2.setGeometry(QtCore.QRect(190, 10, 71, 31))
        self.pick_edit2.setObjectName("pick_edit2")
        self.pick_edit3 = QtWidgets.QTextEdit(self.tab)
        self.pick_edit3.setGeometry(QtCore.QRect(260, 10, 71, 31))
        self.pick_edit3.setObjectName("pick_edit3")
        self.pick_edit4 = QtWidgets.QTextEdit(self.tab)
        self.pick_edit4.setGeometry(QtCore.QRect(330, 10, 71, 31))
        self.pick_edit4.setObjectName("pick_edit4")
        self.pick_edit5 = QtWidgets.QTextEdit(self.tab)
        self.pick_edit5.setGeometry(QtCore.QRect(400, 10, 71, 31))
        self.pick_edit5.setObjectName("pick_edit5")
        self.ban_edit = QtWidgets.QTextEdit(self.tab)
        self.ban_edit.setGeometry(QtCore.QRect(120, 50, 71, 31))
        self.ban_edit.setObjectName("ban_edit")
        self.ban_edit1 = QtWidgets.QTextEdit(self.tab)
        self.ban_edit1.setGeometry(QtCore.QRect(190, 50, 71, 31))
        self.ban_edit1.setObjectName("ban_edit1")
        self.ban_edit2 = QtWidgets.QTextEdit(self.tab)
        self.ban_edit2.setGeometry(QtCore.QRect(260, 50, 71, 31))
        self.ban_edit2.setObjectName("ban_edit2")
        self.ban_edit3 = QtWidgets.QTextEdit(self.tab)
        self.ban_edit3.setGeometry(QtCore.QRect(330, 50, 71, 31))
        self.ban_edit3.setObjectName("ban_edit3")
        self.ban_edit4 = QtWidgets.QTextEdit(self.tab)
        self.ban_edit4.setGeometry(QtCore.QRect(400, 50, 71, 31))
        self.ban_edit4.setObjectName("ban_edit4")
        self.reset_tool = QtWidgets.QPushButton(self.tab)
        self.reset_tool.setGeometry(QtCore.QRect(180, 140, 75, 23))
        self.reset_tool.setObjectName("reset_tool")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../Downloads/anh-nen-tuong-yasuo-4k_040627692.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.email = QtWidgets.QPushButton(self.tab_2)
        self.email.setGeometry(QtCore.QRect(110, 40, 75, 23))
        self.email.setObjectName("email")
        self.Facebook = QtWidgets.QPushButton(self.tab_2)
        self.Facebook.setGeometry(QtCore.QRect(110, 80, 75, 23))
        self.Facebook.setObjectName("Facebook")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cilent AutoPick"))
        self.label.setText(_translate("MainWindow", "Nhập tướng cần pick"))
        self.label_2.setText(_translate("MainWindow", "Nhập tướng cần ban"))
        self.label_3.setText(_translate("MainWindow", "Trạng thái tool"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.reset_tool.setText(_translate("MainWindow", "Tối ưu máy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Đánh rank và thường"))
        self.email.setText(_translate("MainWindow", "Email"))
        self.Facebook.setText(_translate("MainWindow", "Facebook"))
        self.label_4.setText(_translate("MainWindow", "Liên hệ với admin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Liên hệ với Admin và cài đặt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
