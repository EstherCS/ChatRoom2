# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assignment.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Body = QtWidgets.QTextBrowser(self.centralwidget)
        self.Body.setGeometry(QtCore.QRect(30, 110, 261, 221))
        self.Body.setObjectName("Body")
        self.Text = QtWidgets.QLineEdit(self.centralwidget)
        self.Text.setGeometry(QtCore.QRect(30, 340, 261, 31))
        self.Text.setObjectName("Text")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(30, 70, 51, 16))
        self.Name.setObjectName("Name")
        self.InputName = QtWidgets.QTextEdit(self.centralwidget)
        self.InputName.setGeometry(QtCore.QRect(90, 50, 111, 51))
        self.InputName.setObjectName("InputName")
        self.Login = QtWidgets.QPushButton(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(210, 50, 81, 51))
        self.Login.setObjectName("Login")
        self.Send = QtWidgets.QPushButton(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(30, 382, 261, 31))
        self.Send.setObjectName("Send")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
        self.Name.setText(_translate("MainWindow", "NickName"))
        self.Login.setText(_translate("MainWindow", "Login"))
        self.Send.setText(_translate("MainWindow", "Send"))
        self.menuChat_Application.setTitle(_translate("MainWindow", "Chat Application"))

