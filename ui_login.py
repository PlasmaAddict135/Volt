# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginlkFDaw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(584, 382)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.email_entry = QLineEdit(self.centralwidget)
        self.email_entry.setObjectName(u"email_entry")
        self.email_entry.setGeometry(QRect(170, 140, 231, 21))
        self.email_entry.setStyleSheet(u"border-radius: 7px;\n"
"border: 0.5px solid black;\n"
"padding-left: 5px;")
        self.pass_entry = QLineEdit(self.centralwidget)
        self.pass_entry.setObjectName(u"pass_entry")
        self.pass_entry.setGeometry(QRect(170, 170, 231, 21))
        self.pass_entry.setStyleSheet(u"border-radius: 7px;\n"
"border: 0.5px solid black;\n"
"padding-left: 5px;")
        self.pass_entry.setEchoMode(QLineEdit.Password)
        self.login_lbl = QLabel(self.centralwidget)
        self.login_lbl.setObjectName(u"login_lbl")
        self.login_lbl.setGeometry(QRect(240, 80, 91, 41))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(48)
        self.login_lbl.setFont(font)
        self.submit_btn = QPushButton(self.centralwidget)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setGeometry(QRect(250, 210, 75, 23))
        self.submit_btn.setStyleSheet(u"border-radius: 7px;\n"
"border: 0.5px solid black;\n"
"padding-left: 5px;")
        self.registerTransfer = QPushButton(self.centralwidget)
        self.registerTransfer.setObjectName(u"registerTransfer")
        self.registerTransfer.setGeometry(QRect(200, 250, 171, 23))
        self.registerTransfer.setStyleSheet(u"background-color: #f0f0f0;\n"
"border: 0px transparent white;\n"
"color: rgb(3, 83, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 584, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.email_entry.setText("")
        self.email_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.pass_entry.setText("")
        self.pass_entry.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.login_lbl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:22pt;\">LOGIN</span></p></body></html>", None))
        self.submit_btn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.registerTransfer.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
    # retranslateUi

