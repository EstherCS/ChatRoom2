# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Clientui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.people = QtWidgets.QTextEdit(self.centralwidget)
        self.people.setGeometry(QtCore.QRect(0, 0, 711, 71))
        self.people.setObjectName("people")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(10, 100, 51, 16))
        self.Name.setObjectName("Name")
        self.InputName = QtWidgets.QLineEdit(self.centralwidget)
        self.InputName.setGeometry(QtCore.QRect(70, 90, 231, 31))
        self.InputName.setObjectName("InputName")
        self.InputPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.InputPassword.setGeometry(QtCore.QRect(310, 90, 231, 31))
        self.InputPassword.setObjectName("InputPassword")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(550, 90, 151, 31))
        self.Login.setObjectName("Login")
        self.UpdateP = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateP.setGeometry(QtCore.QRect(500, 140, 201, 31))
        self.UpdateP.setObjectName("UpdateP")
        self.CP = QtWidgets.QLabel(self.centralwidget)
        self.CP.setGeometry(QtCore.QRect(10, 150, 91, 16))
        self.CP.setObjectName("CP")
        self.ChangePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.ChangePassword.setGeometry(QtCore.QRect(110, 140, 381, 31))
        self.ChangePassword.setObjectName("ChangePassword")
        self.Body = QtWidgets.QLineEdit(self.centralwidget)
        self.Body.setGeometry(QtCore.QRect(10, 190, 691, 341))
        self.Body.setObjectName("Body")
        self.text = QtWidgets.QLineEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(10, 540, 691, 51))
        self.text.setObjectName("Text")
        self.Send = QtWidgets.QPushButton(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(10, 602, 691, 31))
        self.Send.setObjectName("Send")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 22))
        self.menubar.setObjectName("menubar")
        self.menuChat_Application = QtWidgets.QMenu(self.menubar)
        self.menuChat_Application.setObjectName("menuChat_Application")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuChat_Application.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name.setText(_translate("MainWindow", "NuckName"))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.UpdateP.setText(_translate("MainWindow", "Update Password"))
        self.CP.setText(_translate("MainWindow", "Change Password"))
        self.Send.setText(_translate("MainWindow", "Send"))
        self.menuChat_Application.setTitle(_translate("MainWindow", "Chat Application"))

