# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(371, 457)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(30, 30, 51, 16))
        self.Name.setObjectName("Name")
        self.SInputName = QtWidgets.QLineEdit(self.centralwidget)
        self.SInputName.setGeometry(QtCore.QRect(80, 30, 91, 21))
        self.SInputName.setObjectName("SInputName")
        self.Password = QtWidgets.QLabel(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(180, 30, 47, 12))
        self.Password.setObjectName("Password")
        self.SPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.SPassword.setGeometry(QtCore.QRect(230, 30, 121, 20))
        self.SPassword.setObjectName("SPassword")
        self.SBody = QtWidgets.QTextBrowser(self.centralwidget)
        self.SBody.setGeometry(QtCore.QRect(30, 90, 321, 281))
        self.SBody.setObjectName("SBody")

        self.Add = QtWidgets.QPushButton(self.centralwidget)
        self.Add.setGeometry(QtCore.QRect(30, 60, 321, 23))
        self.Add.setObjectName("Add")
        self.Delete = QtWidgets.QPushButton(self.centralwidget)
        self.Delete.setGeometry(QtCore.QRect(30, 390, 321, 23))
        self.Delete.setObjectName("Delete")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 371, 22))
        self.menubar.setObjectName("menubar")
        self.menuChat_Application = QtWidgets.QMenu(self.menubar)
        self.menuChat_Application.setObjectName("menuChat_Application")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuChat_Application.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name.setText(_translate("MainWindow", "NickName"))
        self.Password.setText(_translate("MainWindow", "Password"))
        self.Add.setText(_translate("MainWindow", "Add"))
        self.Delete.setText(_translate("MainWindow", "Delete"))
        self.menuChat_Application.setTitle(_translate("MainWindow", "Chat Application"))

